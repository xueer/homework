#coding=UTF-8
from sys import argv
# argv��raw_input()����:�û������ʱ����ͬ,������������û�ִ������ʱ����,�Ǿ���argv,����ڽű�ִ�й�������Ҫ�û�����,Ҫ��raw_input(),
# script,first, second, third = argv  


# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

#��ϰ1
# script,name,age,job = argv
# print "The name is",name,
# print "and age is ",age,
# print "and job is",job,'.'

#��ϰ2 
# script, name,age,job,child,yourmather,yourfather = argv
# print "The name is",name,
# print "and age is ",age,
# print "and job is",job,
# print "her is child:",child,yourmather,yourfather


#�ӷ���ϰ  
  
script, first = argv  
  
  
print "How %s are you?" % first  
write = raw_input()  
print "You %s is %s." % (first, write)  

#http://blog.csdn.net/lixiang0522/article/details/7676375
