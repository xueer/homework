#coding=UTF-8

''' 16 处理面包屑主要是获取其层级关系,以及获得当前的层级.找到面包屑所在的div或u然后通过该div或ul找到下面的所有链接,这些链接就是父层级.最后不是链接的部分就应该是当前层级了.
'''

from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('breadcrumb.html')
dr.get(file_path)

# 获得其父层级
for link in dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a'):
	print link.text
	sleep(2)

# 获取当前层级
# 由于页面上可能有很多class为active的元素
# 所以使用层级定位最为保险
print dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text
sleep(3)

dr.quit()