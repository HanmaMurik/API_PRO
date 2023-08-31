import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time
url = 'https://books.toscrape.com/'

# async def parser():
#     result_list = []
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as weber:
#             web = await weber.text()
#             my_bs = BeautifulSoup(web, 'html.parser')
#             response_bs = my_bs.findAll('p', {'class': 'price_color'})
#             for prices in response_bs:
#                 result_list.append(prices.text)
#             print(result_list)
#
# asyncio.run(parser())
# Цена

# async def parser():
#     result_list = []
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as weber:
#             web = await weber.text()
#             my_bs = BeautifulSoup(web, 'html.parser')
#             response_bs = my_bs.findAll('p', {'class': 'instock availability'})
#             for prices in response_bs:
#                 result_list.append(prices.text)
#             print(result_list)
#
# asyncio.run(parser())
# Кол-во

#
# response = requests.get(url)
# content = response.content
#
# soup = BeautifulSoup(content, "html.parser")
#
# li_elements = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
#
# for li_element in li_elements:
#     h3_element = li_element.find("h3")
#     link_element = h3_element.find("a")
#     title = link_element["title"]
#     print(title)
# Название

# async def parser():
#     result_list = []
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as weber:
#             web = await weber.text()
#             my_bs = BeautifulSoup(web, 'html.parser')
#             response_bs = my_bs.findAll('img', {'class': 'thumbnail'})
#             for prices in response_bs:
#                 result_list.append(prices.text)
#                 print(prices.get('src'))
#
#
# asyncio.run(parser())
# Ссылка на фото