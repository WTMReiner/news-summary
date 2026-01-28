from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


@dataclass
class NewsItem:
    number: int | None
    title: str
    summary: str
    keywords: list[str]
    sources: list[str]


def parse_html(html: str) -> list[NewsItem]:
    soup = BeautifulSoup(html, "html.parser")
    items: list[NewsItem] = []
    for card in soup.select(".news-card"):
        number_text = _text(card.select_one(".news-number"))
        number = int(number_text) if number_text.isdigit() else None
        title = _text(card.select_one(".news-title"))
        summary = _text(card.select_one(".news-summary"))
        keywords = [_text(k) for k in card.select(".news-keywords .keyword")]
        sources: list[str] = []
        for a in card.select(".news-source a"):
            href = a.get("href")
            if isinstance(href, str):
                s = href.strip()
                if s:
                    sources.append(s)
        if title and summary:
            items.append(
                NewsItem(
                    number=number,
                    title=title,
                    summary=summary,
                    keywords=[k for k in keywords if k],
                    sources=[s for s in sources if s],
                )
            )
    return items


def parse_file(path: Path | str) -> list[NewsItem]:
    p = Path(path)
    html = p.read_text(encoding="utf-8")
    return parse_html(html)


def _text(node: Tag | NavigableString | None) -> str:
    return (node.get_text(strip=True) if isinstance(node, Tag) else (str(node).strip() if node else "")).strip()
