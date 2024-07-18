from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import re
import html

price_usd_to = 400 

realt = f"https://realt.by/rent/flat-for-long/?addressV2=%5B%7B%22townUuid%22%3A%224cb07174-7b00-11eb-8943-0cc47adabd66%22%7D%5D&page=1&priceTo={price_usd_to}&priceType=840"
response = get(realt)
print(response.status_code)

html_soup = BeautifulSoup(response.text, 'html.parser')


houses_number = html_soup.find('div', class_ = 'justify-between items-center -mx-0 sm:-mx-0 flex flex-wrap md:mb-4 mb-2 !-mr-0.5')
houses_number = houses_number.find('div', class_ = 'flex')
houses_number = int(houses_number.find('b').get_text())

house_container = html_soup.find('div', {'data-index': '0'}).find('div', class_ = 'p-0 bg-white block drop-shadow-none border-basic-200 rounded-md flex flex-col md:flex-row bg-white h-full relative md:h-[374px]')

house_url = 'https://realt.by' + house_container.find('a').get('href')

house_container = house_container.find('div', class_ = 'flex flex-col w-full h-full p-5')

price_usd = house_container.find('span', class_ = 'text-basic text-subhead').text
rooms_num = house_container.find('p', class_ = 'flex flex-wrap text-headline items-center font-semibold md:font-bold -mr-2 mb-2.5 md:mb-4 -order-2 md:-order-none').find('span').text
address = house_container.find_all('div', class_ = 'w-full')[1].find('p', class_ = 'text-basic w-full text-subhead md:text-body').text
subway_station = house_container.find('div', class_ = 'text-basic leading-none mb-2.5 md:mb-4 mt-1 md:mt-0.5 empty:mt-0 children:md:text-body children:text-subhead').find('span', class_ = "mr-4").text

print(house_url)