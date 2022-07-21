from bs4 import BeautifulSoup
import lxml # noqa
import requests
import re


class Shop:
    url_product = ''
    pass


class ShopDigitec(Shop):
    url_product = 'https://www.digitec.ch/de/s1/product/raspberry-pi-zero-2-w-cortex-a53-entwicklungsboard-kit-17346864?supplier=406802' # noqa

    pass


class Pishop(Shop):
    text_not_available = 'Verfügbarkeit: Zur Zeit nicht an Lager'

    def __init__(self, url):
        self.url = url
        self.av_text = ''

    def create_soup(self):
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, 'lxml')
        self.av_text = soup.find('p', class_='availability').text

    def compare_av_negative(self):
        if self.av_text != self.text_not_available:
            print(f'It is available at {self.url}!')
        if self.av_text == self.text_not_available:
            print(f'It is not available at {self.url}')
            pass

    def ask(self):
        self.create_soup()
        self.compare_av_negative()


if __name__ == '__main__':
    print("I'm main")
    my_pishop = Pishop('https://www.pi-shop.ch/raspberry-pi-zero-2-w')
    my_pishop.ask()
