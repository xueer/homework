#coding=UTF-8

''' 04 设置浏览器大小'''

from selenium import webdriver
import time

dr = webdriver.Chrome()

dr.set_window_size(240, 320)
dr.get('http://www.3g.qq.com')

time.sleep(5)
dr.quit()