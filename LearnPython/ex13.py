#coding=UTF-8
from sys import argv
# argv和raw_input()区别:用户输入的时机不同,如果参数是在用户执行命令时输入,那就用argv,如果在脚本执行过程中需要用户输入,要用raw_input(),
# script,first, second, third = argv  


# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

#练习1
# script,name,age,job = argv
# print "The name is",name,
# print "and age is ",age,
# print "and job is",job,'.'

#练习2 
# script, name,age,job,child,yourmather,yourfather = argv
# print "The name is",name,
# print "and age is ",age,
# print "and job is",job,
# print "her is child:",child,yourmather,yourfather


#加分练习  
  
script, first = argv  
  
  
print "How %s are you?" % first  
write = raw_input()  
print "You %s is %s." % (first, write)  

#http://blog.csdn.net/lixiang0522/article/details/7676375
