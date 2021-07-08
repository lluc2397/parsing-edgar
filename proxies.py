import requests
from lxml.html import fromstring

from bs4 import BeautifulSoup


# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr')[:10]:
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies

# proxies = get_proxies()
# print(proxies)

def get_proxies():
    url = f'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # proxy1 = soup.find_all('tr', class_ ='odd' )
    # proxy2 = soup.find_all('tr', class_ ='even' )
    modal = soup.find('div', class_="modal-body" )
    modal_text = modal.textarea.text.replace('Free proxies from free-proxy-list.net', '')
    
    modal_text_clean = modal_text.splitlines()[3:]

    return modal_text_clean

proxy = get_proxies()
print(proxy)
# proxies = get_proxies()

    # proxy = {'http': 'http://' + random.choice(proxies)}

    # new_page = requests.get(new_url, proxies=proxy)