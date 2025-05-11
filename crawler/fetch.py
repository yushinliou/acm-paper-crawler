import requests

def fetch_html(url, headers=None):
    if headers is None: # Use default headers if none provided
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
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(response.headers.get("Content-Type"))
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None
