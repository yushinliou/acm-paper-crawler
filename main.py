import pandas as pd
from crawler.fetch import fetch_html
from crawler.parser import *
from crawler.downloader import download_pdf
from crawler.site_config import SiteConfig
from crawler.config_loader import load_site_configs
import os
import time
import random

def main():
    configs = load_site_configs()
    config = configs['tjs']
    
    os.makedirs(config.download_dir, exist_ok=True)
    df = pd.read_csv(config.csv)

    for _, row in df.iterrows():
        section_title = row[config.title]
        url = row[config.href]
        print(f"Processing: {section_title} -> {url}")

        time.sleep(random.uniform(config.sleep_min, config.sleep_max))  # Sleep for a random time between 1 and 10 seconds
        html = fetch_html(url)
        parser_fn = PARSER_REGISTRY[config.parser]

        if html:
            pdf_links = parser_fn(html, base_url=url)
            for link in pdf_links:
                download_pdf(config, link)
                time.sleep(random.uniform(config.sleep_min, config.sleep_max)) 

if __name__ == "__main__":
    main()
