from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd
import numpy as np
import telegram
from datetime import datetime

# class CheckNewDate:
#     def __init__(self, token, chat_id, url):
            
#         #setting
#         res = requests.get(url)
#         html = res.text
#         self.soup = BeautifulSoup(html, 'html.parser')
#         self.bot = telegram.Bot(token = token)
#         self.chat_id = chat_id
        
#     def request(self):
#         list = self.soup.find_all("div", "col-body")
#         print(list)
        
# if __name__ == "__main__":
token = '5926326529:AAHdf735laL5e2jPF-6zjtYaaH5_KHdIouM'
chat_id = 5814436976
url_new = 'http://ticket.cgv.co.kr/Reservation/Reservation.aspx?MOVIE_CD=20031534&MOVIE_CD_GROUP=20030160&PLAY_YMD=20230102&THEATER_CD=0013&PLAY_NUM=&PLAY_START_TM=1900&AREA_CD=13&SCREEN_CD=01&THIRD_ITEM=&SCREEN_RATING_CD='

# a = CheckNewDate(token, chat_id, url_new)
# a.request()
print(url_new)

res = requests.get(url_new)
print(res)
html = res.text
print(type(html))
soup = BeautifulSoup(html, 'html.parser')
list = soup.find_all("div", "col-body")
print(list)