import os
import requests
from crawler.site_config import SiteConfig
from urllib.parse import urlsplit
from urllib.parse import unquote

def download_pdf(site_config: SiteConfig, url):
    filename = os.path.basename(urlsplit(url).path)
    if not filename.endswith('.pdf'):
        filename += '.pdf'
    if len(filename) > len(str('TJS_71_00.pdf')):
        filename = unquote(filename)
    filepath = os.path.join(site_config.download_dir, filename)
    # add .pdf to the end of the filename if it doesn't exist

    if os.path.exists(filepath):
        print(f"Already downloaded: {filename}")
        return

    try:
        response = requests.get(url, stream=True, headers=site_config.headers, timeout=15)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
