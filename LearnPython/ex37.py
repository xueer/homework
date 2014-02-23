#coding=UTF-8
keywords=['and','del','from','not','while','as','elif','global','or','with','assert','else','if','pass','yield','break','except','import','print','class','exec','in','raise','continue','finally','is','return','def','for','lambda','try']

datatypes=['True','False','None','strings','numbers','floats','lists']

# \\斜杠 \' 单引号 \"双引号 \a响铃 \b 退格符 \n换行符 \r回车符 \f换页符   \t横向制表符   \v 纵向制表符
# \e 转义 \000空  \(行尾时) 续行符  
# 不想让转义符生效果,用r或R定义原始字符串
str1="\aescape sequences this is a pen.c:\\book\'ABC\'test"\
"lesson1"
str2='\bHow are you, I said: \"what\'s are you doing ? \" \nadfwerwe'
print str1
print str2
print "\a"
print r"\n"
print "scale is 80%"
print "ABC\tDEFG"  #\t作用如tab键

print "Number\tSquare\tCube"
for i in range(1,11):
	print i,'\t',i**2,'\t',i**3




# 加,号,输出两个字符串之间有个空格
print "a",
print "b"
# +号,则没有空格
print "a" + "b"



# %d 有符号整数(十进制)  %i 有符号整数(十进制)     %u 无符号整数(十进制)     %o 无 符号整数(八进制)
# %x 无符号整数(16进制)  %X 无符号整数(16进制大写)  %e 浮点数(科学计数法)    %E 浮点数(用E表示)
# %f 浮点数(小数点)      %F  浮点数(小数点)        
# %g 浮点数(根据值的大小采用%e或%f)             %G 浮点数(类似%g)
# %c  格式化字符及其ASCII码    %r 字符串(转换python对象用repr())     %s 字符串(转换python对象用str())   
#%% 百分号标记
name = "mary"
print "my name is %s" % name

age=323454252342342342342342342424
print "I am is %i years old" % age
print "I am is %d years old" % age

i=13.4
print "the num is %f" %i
print "the num is %F" %i

s=12.54753
print "%.8f" %s  #不足位数用0补
print "%.2f" %s  # 四舍五入

print "%i" %s     #直接截断
print "%d" %s

num1=12.1
num2=456712345.6
print "%g" % num1
print "%g" % num2  #g数大时会自动选择e计法


#%r和%s区别,%r原样输出
str3="hello,\nworld"
print "this is test1:%% %s" %str3
print "this is test2:%r" %str3
print "%c" %72

#操作符 
a=3
b=3
c=4
c**= a   #乘方运算  c=c**a  
b**=a
print c


# /除法  //整除  **乘方 %取余