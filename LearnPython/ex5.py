#coding=UTF-8
my_name = 'marysnow'
my_age = 32
my_age -= 1  #相当于my_age=my_age-1
my_height = 65

my_weight = 175
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print my_age
print "Let's talk about %s." % my_name    #%s字符串,%d整数,%o整数(八进制),%x(16进制数), %f(浮点数)
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age,my_height,my_weight,my_age+my_height+my_weight)

print "输出: %r  %r  %r  %r" %(my_name,my_eyes,my_teeth,my_age) #%r是一个万能的格式符，它会将后面给的参数原样打印出来，带有类型信息.