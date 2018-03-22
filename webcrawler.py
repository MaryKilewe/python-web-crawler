import requests

from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page_code = 0
    page = 1
    while page <= max_pages:
        url = 'https://www.ebay.com/sch/Cell-Phones-Smartphones/9355/i.html?_pgn=' + str(page) + '&_skc=' + str(page_code) + '&rt=nc'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class':'vip'}):
            href = link.get('href')
            # print(href)
            title = link.string
            print(title)
            print(href)
            get_single_item_data(href)
        page += 1
        page_code += 50


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('span', {'id':'prcIsum'}):
        print(item_name.string)



trade_spider(2)
