from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import re
import html

class Scraping:
    def __init__(self, price):
        self._price_to = price

    def url(self):
        return 'https://weekend.by/minsk/arenda-kvartir-na-dlitelniy-srok?sort=price'   #another site

    @property
    def price_to(self):
        return self._price_to

    @price_to.setter
    def change_price_to(self, new_price):
        if new_price > 0:
            self._price_to = new_price

    def get_soup(self):
        url = self.url()
        response = get(url)
        if response.status_code == 200:
            html_soup = BeautifulSoup(response.text, 'html.parser')
            titles = ['price_usd', 'price_byn', 'address', 'rooms_num', 'publication_date']
            df = pd.DataFrame(columns=titles)
            houses = html_soup.find('div', class_ = 'posts-list').find_all('div', class_ = 'col-12d')
            for house in houses:
                rooms_num = house.find('div', class_ = 'related_title').find('a').text
                rooms_num = rooms_num.split(',')[0]

                price_byn = house.find('div', class_ = 'price').find('span', class_ = 'pia_link').find('span').text

                price_usd = house.find('div', class_ = 'price').find('span', class_ = 'doppric').text

                address = house.find('div', class_ = 'info').find('div', class_ = 'probegla').text

                appending_row = [price_usd, price_byn, address, rooms_num]
                df_len = len(df)
                df.loc[df_len] = appending_row
            return df
        else:
            return False    
        
newScrap = Scraping(400)
df = newScrap.get_soup()
print(df)