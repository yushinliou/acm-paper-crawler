from bs4 import BeautifulSoup
from urllib.parse import urljoin

# all parser in here
def chi_parser(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []
    for a_tag in soup.find_all('a', href=True, attrs={'aria-label': 'PDF'}):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        pdf_links.append(full_url)
    return pdf_links

def tjs_parser(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('.pdf'):
            # Check if the link is a PDF
            full_url = urljoin(base_url, href)
            pdf_links.append(full_url)
    return pdf_links
# parser registry
PARSER_REGISTRY = {
    'chi_parser': chi_parser,
    'tjs_parser': tjs_parser
}


# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def extract_pdf_links(html, base_url):
#     soup = BeautifulSoup(html, 'html.parser')
#     pdf_links = []
#     for a_tag in soup.find_all('a', href=True, attrs={'aria-label': 'PDF'}):
#         href = a_tag['href']
#         full_url = urljoin(base_url, href)
#         pdf_links.append(full_url)
#     return pdf_links


