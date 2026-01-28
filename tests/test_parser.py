from pathlib import Path

from news_summary.parser import parse_file


def test_parse_sample_report():
    sample = Path("Report/Reiner-AI-信息差-2026-01-28.html")
    assert sample.exists(), "示例报告文件不存在"
    items = parse_file(sample)
    assert len(items) == 6
    first = items[0]
    assert "OpenAI" in first.title
    assert first.sources, "应包含至少一个来源链接"
