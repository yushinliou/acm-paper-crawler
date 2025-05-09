import os

# Define the directory and file structure
base_dir = "/Users/liuyuxin/Programming/paper-crawler"
files = {
    "main.py": """\
import pandas as pd
from fetch import fetch_html
from parser import extract_pdf_links
from downloader import download_pdf
from settings import DOWNLOAD_DIR
import os

def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    df = pd.read_csv('your_csv_file.csv')

    for _, row in df.iterrows():
        section_title = row['section__title']
        url = row['section__title href']
        print(f"Processing: {section_title} -> {url}")

        html = fetch_html(url)
        if html:
            pdf_links = extract_pdf_links(html, base_url=url)
            for link in pdf_links:
                download_pdf(link)

if __name__ == "__main__":
    main()
""",

    "fetch.py": """\
import requests

def fetch_html(url, headers=None):
    headers = headers or {
        "User-Agent": "Mozilla/5.0 (compatible; PaperBot/1.0)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None
""",

    "parser.py": """\
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_pdf_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('.pdf'):
            full_url = urljoin(base_url, href)
            pdf_links.append(full_url)
    return pdf_links
""",

    "downloader.py": """\
import os
import requests
from settings import DOWNLOAD_DIR
from urllib.parse import urlsplit

def download_pdf(url):
    filename = os.path.basename(urlsplit(url).path)
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    if os.path.exists(filepath):
        print(f"Already downloaded: {filename}")
        return

    try:
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
""",

    "settings.py": """\
DOWNLOAD_DIR = "downloads"
""",

    "utils.py": """\
# Reserved for shared helper functions, if needed later
""",

    "requirements.txt": """\
pandas
requests
beautifulsoup4
"""
}

# Create the base directory and write the files
os.makedirs(base_dir, exist_ok=True)
for filename, content in files.items():
    with open(os.path.join(base_dir, filename), "w") as f:
        f.write(content)

# Output the directory path
base_dir