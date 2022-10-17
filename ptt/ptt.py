import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'

r = requests.get('https://disp.cc/b/')
soup = BeautifulSoup(r.text, 'html.parser')  # .text會存下html
spans = soup.find_all('span', class_='ht_title')  # 會回傳整個tag, class本身在python補能用，還是想用要在後面加底線class_
for s in spans:
    href = s.find('a').get('href')
    url = root_url + href
    title = s.text

    print(f'{title}\n{url}')
