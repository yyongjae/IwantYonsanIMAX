from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests
import time
import csv
import pandas as pd
import numpy as np
import telegram
from datetime import datetime
from time import process_time, sleep

class IwantIMAX:
    def __init__(self, driver, agent, token, chat_id):
        
        #setting
        self.driver = driver
        self.agent = agent
        self.headers = {'User-Agent': self.agent}
        self.browser = webdriver.Chrome(self.driver)
        self.bot = telegram.Bot(token = token)
        self.chat_id = chat_id

    def checkNewDate(self, url, date):
        print("start to check new schedule..")
        
        self.browser.get(url)
        
        day_list = self.browser.find_element_by_xpath('//*[@id="ticket"]/div[2]/div[1]/div[3]/div[2]').text
        print(day_list)
        flag = True
        try:
            while flag:
                now = datetime.now()
                
                if date in day_list:
                    try:
                        begin = 0
                        while True:
                            self.bot.sendMessage(chat_id = self.chat_id, text = "가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자")
                            print("Send Message")
                            
                            if begin < 10:
                                sleep(1)
                                begin+=1
                                continue
                            else:
                                flag = False
                                break
                            
                    except:
                        print("Fail to send")

                if now.second == 0:
                    self.browser.refresh()
        except:
            self.bot.sendMessage(chat_id = self.chat_id, text = "DIE")
            print("DIE...")
        
        
if __name__ == "__main__":
    
    driver = None
    agent = None
    token = None
    chat_id = None
    url_old = 'http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0013&date=20230103'
    url_new = 'http://ticket.cgv.co.kr/Reservation/Reservation.aspx?MOVIE_CD=20031534&MOVIE_CD_GROUP=20030160&PLAY_YMD=20230102&THEATER_CD=0013&PLAY_NUM=&PLAY_START_TM=1900&AREA_CD=13&SCREEN_CD=01&THIRD_ITEM=&SCREEN_RATING_CD='
    date = '수\n11'
    
    yongmax = IwantIMAX(driver, agent, token, chat_id)
    yongmax.checkNewDate(url_new, date)
    