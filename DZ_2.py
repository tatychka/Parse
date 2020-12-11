import time
import requests
import bs4


class MagnitParse:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }

    def __init__(self, start_url):
        self.start_url=start_url


    @staticmethod
    def _get(self, *args, **kwargs):
        while True:
            try:
                response = requests.get(*args, **kwargs)
                if response.status_code != 200:
                    raise Exception
                return response
            except Exception:
                time.sleep(0.5)

    def run(self):
        a = self._get(self.start_url, headers=self.headers)
        print(1)

    def parse(self):
        pass

    def save(self):
        pass


if __name__ =='__main__':
    parser = MagnitParse('https://magnit.ru/promo/?geo=moskva')
    parser.run()