from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_pdf_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []
    for a_tag in soup.find_all('a', href=True, attrs={'aria-label': 'PDF'}):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        pdf_links.append(full_url)
    return pdf_links

