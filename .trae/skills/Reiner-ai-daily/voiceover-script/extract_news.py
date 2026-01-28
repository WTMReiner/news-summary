import argparse
import json
import sys
from bs4 import BeautifulSoup

def extract_news(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(html_content, 'html.parser')
    cards = soup.find_all('div', class_='card')
    
    news_items = []
    for card in cards:
        headline_div = card.find('div', class_='headline')
        summary_div = card.find('div', class_='summary')
        meta_div = card.find('div', class_='meta')
        
        if headline_div and summary_div:
            headline = headline_div.get_text(strip=True)
            summary = summary_div.get_text(strip=True)
            source = meta_div.get_text(strip=True) if meta_div else "Unknown Source"
            
            news_items.append({
                "headline": headline,
                "summary": summary,
                "source": source
            })
    
    return news_items

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract news from Reiner AI Daily HTML')
    parser.add_argument('file_path', help='Path to the HTML file')
    args = parser.parse_args()

    items = extract_news(args.file_path)
    print(json.dumps(items, ensure_ascii=False, indent=2))
