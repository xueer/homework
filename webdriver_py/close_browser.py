#coding=UTF-8

''' 02 关闭浏览器'''

from selenium import webdriver
import time

dr = webdriver.Chrome()
time.sleep(2)
print 'browser will be closed'
dr.quit() # or dr.close()
print 'browser is closed'
