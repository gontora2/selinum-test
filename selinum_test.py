from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# import pandas as pd

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options) 

url = "https://news.google.com/topstories?tab=wn&hl=ja&gl=JP&ceid=JP:ja"
browser.get(url)
w = browser.execute_script('return document.body.scrollWidth')
h = browser.execute_script('return document.body.scrollHeight')
w= 1400
h=900
browser.set_window_size(w, h)
c
time.sleep(1)

#kw = browser.find_element_by_name("kw")
#kw.clear()
#kw.send_keys("製品")
#
#kw.send_keys(Keys.ENTER);
browser.save_screenshot("test.png")
#search = browser.find_element_by_class_name("btn-item")
#search.click
