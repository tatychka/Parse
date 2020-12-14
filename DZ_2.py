import time
import requests
import bs4
from urllib.parse import urljoin
# совмещение юрлов
product = {
            'url': lambda soup: '',
            'promo_name': '',
            'product_name': '',
            'image_url': '',
        }
class MagnitParse:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }

    def __init__(self, start_url):
        self.start_url = start_url

        self.product_template = {
            'url': lambda soup: urljoin(self.start_url, soup.get('href')),
            'promo_name': lambda soup: soup.find('div', attrs={'class': 'card-sale__header'}).text,
            'product_name': lambda soup: soup.find('div', attrs={'class': 'card-sale__title'}).text,
            'image_url': lambda soup: urljoin(self.start_url, soup.find('img').get('data-src')),
        }

    @staticmethod
    def _get(*args, **kwargs):
        while True:
            try:
                response = requests.get(*args, **kwargs)
                if response.status_code != 200:
                    raise Exception
                return response
            except Exception:
                time.sleep(0.5)

    def soup(self, url):
        response = self._get(url, headers=self.headers)
        return bs4.BeautifulSoup(response.text, 'lxml')

    def run(self):

        soup = self.soup(self.start_url)
        for product in self.parse(soup):
            self.save(product)
            print(1)

    def parse(self, soup) -> dict:
        catalog = soup.find('div', attrs={'class': 'сatalogue__main'})

        for product in catalog.find_all('a', recursive=False):
            pr_data = self.get_product(product)
            yield pr_data

    def get_product(self, product_soup):

        result = {}
        for key, value in self.product_template.items():
            result[key] = value(product_soup)
        return result

    def save(self, product):
        print(1)


if __name__ =='__main__':
    parser = MagnitParse('https://magnit.ru/promo/?geo=moskva')
    parser.run()