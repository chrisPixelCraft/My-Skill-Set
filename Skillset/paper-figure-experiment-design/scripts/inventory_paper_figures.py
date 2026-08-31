#!/usr/bin/env python3
"""Inventory figure captions in PDFs without modifying the source corpus."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


FIGURE_START = re.compile(r"^\s*(?:Figure|Fig\.)\s*(\d+)\s*[:.]\s*(.*)$", re.IGNORECASE)
COPY_PDF_LINK = re.compile(r"\[Copy\]\(<([^>]+\.pdf)>\)|\[Copy\]\(([^)]+\.pdf)\)", re.IGNORECASE)
PDF_LINK = re.compile(r"\[[^]]*\]\(<([^>]+\.pdf)>\)|\[[^]]*\]\(([^)]+\.pdf)\)", re.IGNORECASE)
XHTML_NAMESPACE = {"x": "http://www.w3.org/1999/xhtml"}


@dataclass(frozen=True)
class FigureRecord:
    paper: str
    pdf: str
    figure: int | None
    pdf_page: int | None
    caption: str
    suggested_job: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract a reviewable figure-caption inventory from PDFs, directories, or Markdown manifests."
    )
    parser.add_argument("inputs", nargs="+", type=Path, help="PDF, directory, or Markdown manifest")
    parser.add_argument("--max-figures", type=int, default=3, help="maximum figure number per paper (default: 3)")
    parser.add_argument(
        "--format",
        choices=("markdown", "jsonl", "tsv"),
        default="markdown",
        help="output format (default: markdown)",
    )
    parser.add_argument("--output", type=Path, help="write to this file instead of stdout")
    return parser.parse_args()


def pdfs_from_input(path: Path) -> Iterable[Path]:
    path = path.expanduser().resolve()
    if path.is_dir():
        yield from sorted(p for p in path.rglob("*.pdf") if p.is_file())
        return
    if path.suffix.lower() == ".pdf":
        yield path
        return
    if path.suffix.lower() in {".md", ".markdown"}:
        text = path.read_text(encoding="utf-8", errors="replace")
        copy_matches = list(COPY_PDF_LINK.finditer(text))
        matches = copy_matches or list(PDF_LINK.finditer(text))
        for match in matches:
            target = match.group(1) or match.group(2)
            candidate = (path.parent / target).resolve()
            if candidate.is_file():
                yield candidate
        return
    raise ValueError(f"Unsupported input: {path}")


def extract_bbox_xml(pdf: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-bbox-layout", str(pdf), "-"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        detail = result.stderr.strip() or f"exit code {result.returncode}"
        raise RuntimeError(f"pdftotext failed for {pdf}: {detail}")
    return result.stdout


def classify_job(caption: str) -> str:
    text = caption.lower()
    if any(word in text for word in ("failure", "limitation", "motivation", "collapse", "challenge")):
        return "failure-or-motivation"
    if any(word in text for word in ("benchmark", "taxonomy", "task suite", "dataset")):
        return "benchmark-or-taxonomy"
    if any(word in text for word in ("overview", "framework", "architecture", "pipeline", "workflow")):
        return "method-overview"
    if any(word in text for word in ("comparison", "unlike", "versus", "vs.")):
        return "paradigm-comparison"
    if any(word in text for word in ("accuracy", "performance", "scaling", "speedup", "latency", "ablation")):
        return "outcome-or-scaling"
    if any(word in text for word in ("example", "case study", "qualitative", "visualization")):
        return "capability-or-case"
    return "unclassified"


def extract_records(pdf: Path, max_figures: int) -> list[FigureRecord]:
    records: list[FigureRecord] = []
    xml_text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", extract_bbox_xml(pdf))
    try:
        document = ET.fromstring(xml_text)
    except ET.ParseError as error:
        raise RuntimeError(f"Could not parse pdftotext XML for {pdf}: {error}") from error
    pages = document.findall(".//x:page", XHTML_NAMESPACE)
    seen: set[int] = set()
    for page_number, page in enumerate(pages, start=1):
        for block in page.findall(".//x:block", XHTML_NAMESPACE):
            lines: list[str] = []
            for line in block.findall("./x:line", XHTML_NAMESPACE):
                words = [word.text or "" for word in line.findall("./x:word", XHTML_NAMESPACE)]
                if words:
                    lines.append(" ".join(words))
            block_text = re.sub(r"\s+", " ", " ".join(lines)).strip()
            match = FIGURE_START.match(block_text)
            if not match:
                continue
            figure_number = int(match.group(1))
            if figure_number > max_figures or figure_number in seen:
                continue
            caption = match.group(2).strip()
            records.append(
                FigureRecord(
                    paper=pdf.stem,
                    pdf=str(pdf),
                    figure=figure_number,
                    pdf_page=page_number,
                    caption=caption,
                    suggested_job=classify_job(caption),
                )
            )
            seen.add(figure_number)
    return sorted(records, key=lambda item: item.figure)


def render(records: list[FigureRecord], output_format: str) -> str:
    if output_format == "jsonl":
        return "\n".join(json.dumps(asdict(record), ensure_ascii=False) for record in records)
    if output_format == "tsv":
        header = "paper\tpdf\tfigure\tpdf_page\tsuggested_job\tcaption"
        rows = [
            "\t".join(
                (
                    record.paper,
                    record.pdf,
                    "" if record.figure is None else str(record.figure),
                    "" if record.pdf_page is None else str(record.pdf_page),
                    record.suggested_job,
                    record.caption.replace("\t", " "),
                )
            )
            for record in records
        ]
        return "\n".join((header, *rows))
    rows = ["| Paper | Fig. | PDF page | Suggested job | Caption |", "|---|---:|---:|---|---|"]
    for record in records:
        caption = record.caption.replace("|", "\\|")
        paper = record.paper.replace("|", "\\|")
        figure = "—" if record.figure is None else str(record.figure)
        page = "—" if record.pdf_page is None else str(record.pdf_page)
        rows.append(
            f"| {paper} | {figure} | {page} | {record.suggested_job} | {caption} |"
        )
    return "\n".join(rows)


def main() -> int:
    args = parse_args()
    if args.max_figures < 1:
        raise ValueError("--max-figures must be at least 1")
    if shutil.which("pdftotext") is None:
        raise RuntimeError("pdftotext is required; install Poppler before running this script")

    pdfs = sorted({pdf for source in args.inputs for pdf in pdfs_from_input(source)})
    if not pdfs:
        raise RuntimeError("No readable PDF files were found")

    records: list[FigureRecord] = []
    failures: list[str] = []
    for pdf in pdfs:
        try:
            extracted = extract_records(pdf, args.max_figures)
            if extracted:
                records.extend(extracted)
            else:
                records.append(
                    FigureRecord(
                        paper=pdf.stem,
                        pdf=str(pdf),
                        figure=None,
                        pdf_page=None,
                        caption="",
                        suggested_job="not-detected",
                    )
                )
        except RuntimeError as error:
            failures.append(str(error))

    output = render(records, args.format) + "\n"
    if args.output:
        args.output.expanduser().resolve().write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)

    for failure in failures:
        print(f"warning: {failure}", file=sys.stderr)
    if not records:
        return 2
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
