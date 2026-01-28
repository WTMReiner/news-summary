from __future__ import annotations

import argparse
import json
from pathlib import Path

from .logging_config import configure_logging
from .parser import parse_file


def main() -> None:
    parser = argparse.ArgumentParser(prog="news-summary", description="AI新闻HTML解析与导出")
    parser.add_argument(
        "html_path",
        type=str,
        help="HTML报告路径，例如 Report/Reiner-AI-信息差-2026-01-28.html",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="",
        help="输出JSON文件路径；不提供则打印到stdout",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="输出详细日志",
    )
    args = parser.parse_args()

    configure_logging(verbose=args.verbose)

    items = parse_file(args.html_path)
    data = [
        {
            "number": item.number,
            "title": item.title,
            "summary": item.summary,
            "keywords": item.keywords,
            "sources": item.sources,
        }
        for item in items
    ]

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
