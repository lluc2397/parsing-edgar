import requests
from lxml.html import fromstring

from bs4 import BeautifulSoup

def get_proxies():
    url = f'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    modal = soup.find('div', class_="modal-body" )
    modal_text = modal.textarea.text.replace('Free proxies from free-proxy-list.net', '')
    
    modal_text_clean = modal_text.splitlines()[3:]

    return modal_text_clean

proxy = get_proxies()
print(proxy)
# proxies = get_proxies()

    # proxy = {'http': 'http://' + random.choice(proxies)}

    # new_page = requests.get(new_url, proxies=proxy)