import os
import requests
from settings import DOWNLOAD_DIR
from urllib.parse import urlsplit

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
    "TE": "Trailers",
    "Pragma": "no-cache",
    "DNT": "1",
    "X-Requested-With": "XMLHttpRequest",
    "If-None-Match": "W/\"5d8-5a2f4b0c3e1b0\"",
    "Range": "bytes=0-",
    "If-Range": "W/\"5d8-5a2f4b0c3e1b0\"",
}

def download_pdf(url):
    filename = os.path.basename(urlsplit(url).path)
    if not filename.endswith('.pdf'):
        filename += '.pdf'
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    # add .pdf to the end of the filename if it doesn't exist

    if os.path.exists(filepath):
        print(f"Already downloaded: {filename}")
        return

    try:
        response = requests.get(url, stream=True, headers=headers, timeout=15)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
