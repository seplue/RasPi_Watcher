from bs4 import BeautifulSoup
import lxml
import requests
import re
import time

print('started')
print('Last checked:')

while True:
    # pi-shop.ch
    url_pishop_zero2 = 'https://www.pi-shop.ch/raspberry-pi-zero-2-w?src=raspberrypi'
    url_pishop_control = 'https://www.pi-shop.ch/raspberry-pi-zero-2-w-starter-kit'
    url = url_pishop_zero2

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    av_text = soup.find('p', class_='availability').text

    # print(av_text)
    if av_text != 'Verfügbarkeit: Zur Zeit nicht an Lager':
        print(f'Its available at {url}!')
    if av_text == 'Verfügbarkeit: Zur Zeit nicht an Lager':
        # print(f'Its not available at {url}')
        pass

    # berrybase.ch
    url_berrybase_zero2 = 'https://www.berrybase.ch/detail/index/sArticle/9202?src=raspberrypi'
    url_berrybase_control = ''
    url = url_berrybase_zero2

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    product = soup.find('div', class_='content product--details')
    av_text = product.find('div', class_='alert--content').text

    # print(av_text)
    if av_text != ' Dieser Artikel steht derzeit nicht zur Verfügung! ':
        print(f'Its available at {url}!')
    if av_text == ' Dieser Artikel steht derzeit nicht zur Verfügung! ':
        # print(f'Its not available at {url}')
        pass

    # welectron.com
    url_welectron_na = 'https://www.welectron.com/Raspberry-Pi-Zero-W-mit-loser-Stiftleiste'  # status 0 = not available
    url_welectron_zero2 = 'https://www.welectron.com/Raspberry-Pi-Zero-2-W'  # status 1 = on the way
    url_welectron_a = 'https://www.welectron.com/Raspberry-Pi-Pico'  # status 2 = available
    url = url_welectron_zero2

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    print('bei welectron:', end='\r')
    status_0 = soup.find('span', class_='status status-0')
    if status_0:
        # print(f'It is "{status_0.text}" at {url}')
        pass
    status_1 = soup.find('span', class_='status status-1')
    if status_1:
        # print(f'It is "{status_1.text}" at {url}')
        pass
    status_2 = soup.find('span', class_='status status-2')
    if status_2:
        print(f'It is "{status_2.text}" at {url}')

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f'\r{current_time}', end='')

    time.sleep(60)
