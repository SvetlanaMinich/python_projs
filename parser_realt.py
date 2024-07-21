from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import re
import html

class Scraping:
    def url(self, page):
        return f'https://weekend.by/minsk/arenda-kvartir-na-dlitelniy-srok?sort=-created_at&page={page}&per-page=42'   #another site

    def get_soup(self):
        titles = ['price_usd', 'price_byn', 'subway_stat', 'rooms_num', 'publication_date']
        df = pd.DataFrame(columns=titles)
        for i in range(1,11):
            url = self.url(i)
            response = get(url)
            if response.status_code == 200:
                html_soup = BeautifulSoup(response.text, 'html.parser')
                houses = html_soup.find('div', class_ = 'grid-of-cards__inner mdc-layout-grid__inner').find_all('div', class_ = 'mdc-layout-grid__cell mdc-layout-grid__cell--span-12-tablet mdc-layout-grid__cell--span-12-desktop')
                for house in houses:
                    content = house.find('div', class_ = 'list-card__content')

                    subway_stat = content.find('div', class_ = 'list-card__header').find('h3', class_ = 'list-card__subtitle mdc-typography mdc-typography--subtitle2').text.split('\n')[2].replace(" ","")[:-1]

                    price_usd = content.find('div', class_ = 'list-card__primary').find('div', class_ = 'hidden-xs list-card__price mdc-typography mdc-typography--headline6').text.split('\n')[1].replace(" ","")

                    price_byn = content.find('div', class_ = 'list-card__primary').find('div', class_ = 'hidden-xs list-card__price mdc-typography mdc-typography--headline6').find('div', class_ = 'list-card__price-caption mdc-typography--caption').text.split('\n')[1].replace(" ","")
                    
                    rooms_num = content.find('div', class_ = 'list-card__secondary mdc-typography mdc-typography--body2').text.split('\n')[1].replace(" ","")
                    
                    publication_date = content.find('div', class_ = 'list-card__secondary mdc-typography mdc-typography--body2').find_all('span')[-1].text.split('\n')[1].replace(" ","")

                    appending_row = [price_usd, price_byn, subway_stat, rooms_num, publication_date]
                    df_len = len(df)
                    df.loc[df_len] = appending_row
            else:
                if df.empty:
                    return False
                return df   
        return df
        
newScrap = Scraping()
df = newScrap.get_soup()
df.to_csv(r'C:\python_projs\parser.csv', index=False)