import requests
from bs4 import BeautifulSoup
import csv

# url страницы
url = 'https://auto.ru/cars/new/group/hongqi/hs5/23409476-23409517/?in_stock=IN_STOCK&sort=price-asc&page=1&output_type=list'

# Загружаем страницу
response = requests.get(url)
# Проверка страницы на загруженность
response.raise_for_status() 

print(response)

soup = BeautifulSoup(response.text, features: 'html.parser')
print(soup)

