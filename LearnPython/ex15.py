#coding=UTF-8
from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Type the filename again:"
#file_again = raw_input("> ")
#txt_again = open(file_again)

txt_again = open("readme.txt")
print txt_again.read()    #读取文件内容
#print txt_again.readline() #读取文本文件中的一行

txt_again.close()  #关闭文件
