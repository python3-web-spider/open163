# coding: utf8
# 爬取网易公开课的全部视频
# 单线程，单进程版
# 需要安装 selenium 和 ChromeDriver 、you-get
import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    url = 'https://c.open.163.com/search/search.htm?query=&enc=%E2%84%A2#/search/video'
    browser.get(url)
    for i in range(250):
        print('The ' + str(i+1) + ' page.')
        video_urls = browser.find_elements_by_css_selector('.f-c3.f-f0')
        for index, video_url in enumerate(video_urls):
            print(str(i * 20 + index+1) + '. ' + video_url.get_attribute('href'))
            os.system("you-get " + video_url.get_attribute('href')) # 使用 you-get 下载视频

        # scroll to the buttom
        # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # time.sleep(random.random())
        next_page = browser.find_element_by_css_selector('.znxt')
        next_page.click() # 点击下一页
finally:
    browser.close()
