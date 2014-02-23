#coding=UTF-8

'''30 超时设置'''

ff = webdriver.Firefox()
ff.implicitly_wait(10) # seconds
ff.get("http://somedomain/url_that_delays_loading")
myDynamicElement = ff.find_element_by_id("myDynamicElement")