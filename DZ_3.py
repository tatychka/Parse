from typing import Tuple
import bs4
import requests
from urllib.parse import urljoin


class GbBlogParse:

    def __init__(self, start_url):
        self.start_url = start_url
        self.page_done = set()

    def _get(self, url):
        response = requests.get(url)
        self.page_done.add(url)
        return bs4.BeautifulSoup(response.text, 'lxml')

    def run(self, url=None):
        if not url:
            url = self.start_url

        if url not in self.page_done:
            soup = self._get(url)
            posts, pagination = self.parse(soup)

    def parse(self, soup):
        print(1)


if __name__ ==  '__main__':
    parser = GbBlogParse('https://geekbrains.ru/posts')
    parser.run()