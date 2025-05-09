import pandas as pd
from fetch import fetch_html
from parser import extract_pdf_links
from downloader import download_pdf
from settings import DOWNLOAD_DIR
import os
import time
import random

def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    df = pd.read_csv('./data/head.csv')

    for _, row in df.iterrows():
        section_title = row['section__title']
        url = row['section__title href']
        print(f"Processing: {section_title} -> {url}")

        time.sleep(random.uniform(1, 5))  # Sleep for a random time between 1 and 5 seconds
        html = fetch_html(url)
        if html:
            pdf_links = extract_pdf_links(html, base_url=url)
            for link in pdf_links:
                download_pdf(link)
                time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    main()
