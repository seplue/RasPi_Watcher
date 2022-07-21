from bs4 import BeautifulSoup
import lxml # noqa
import requests
import re


class Shop:
    soup = ''
    av_text = ''
    text_not_available = ''

    def __init__(self, url):
        self.url = url

    def get_soup(self):
        source = requests.get(self.url).text
        self.soup = BeautifulSoup(source, 'lxml')

    def make_av_text(self):
        pass  # will be overwritten by child class, is (for now) specific to child class

    def compare_av_negative(self):
        # todo compare also to text_available to be more sure of it's availability
        if self.av_text != self.text_not_available:
            print(f'It is available at {self.url}!')
        if self.av_text == self.text_not_available:
            print(f'It is not available at {self.url}')
            pass

    def ask(self):
        self.get_soup()
        self.make_av_text()
        self.compare_av_negative()


class ShopDigitec(Shop):
    url_product = 'https://www.digitec.ch/de/s1/product/raspberry-pi-zero-2-w-cortex-a53-entwicklungsboard-kit-17346864?supplier=406802' # noqa

    pass


class Pishop(Shop):
    text_not_available = 'Verfügbarkeit: Zur Zeit nicht an Lager'

    def make_av_text(self):
        self.av_text = self.soup.find('p', class_='availability').text
        if self.av_text == '':
            print('av_text is empty! Has it not been found?')  # todo replace with assert, try or throw error


class Berrybase(Shop):
    text_not_available = ' Dieser Artikel steht derzeit nicht zur Verfügung! '

    def make_av_text(self):
        product = self.soup.find('div', class_='content product--details')
        self.av_text = product.find('div', class_='alert--content').text
        if self.av_text == '':
            print('av_text is empty! Has it not been found?')  # todo replace with assert, try or throw error


if __name__ == '__main__':
    print("I'm main")
    my_pishop = Pishop('https://www.pi-shop.ch/raspberry-pi-zero-2-w')
    my_pishop.ask()

    my_p_pishop = Pishop('https://www.pi-shop.ch/raspberry-pi-zero-2-w-starter-kit')
    my_p_pishop.ask()

    my_berrybase = Berrybase('https://www.berrybase.ch/detail/index/sArticle/9202')
    my_berrybase.ask()

    my_berrybase = Berrybase('https://www.berrybase.ch/dht22-digitaler-temperatur-und-luftfeuchtesensor?c=98')
    my_berrybase.ask()


