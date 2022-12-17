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
        
        self.browser.get(url)
        # browser.implicitly_wait(3)
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, "//*[@id='ifrm_movie_time_table']"))
        day_list = self.browser.find_element_by_id('slider').text
        
        while True:
            now = datetime.now()
            
            if date in day_list:
                self.bot.sendMessage(chat_id = self.chat_id, text = "가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자가보자")
                break

            if now.second == 0:
                self.browser.refresh()

            if now.hour % 6 == 0:
                self.bot.sendMessage(chat_id = self.chat_id, text = "형 나 힘들어")
        
        
if __name__ == "__main__":
    
    driver = '/Users/yongcho/dev/chromedriver_mac_arm64/chromedriver'
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    token = '__'
    chat_id = "__"
    url_new = 'http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0013&date=20230103'
    
    yongmax = IwantIMAX(driver, agent, token, chat_id, url_new)