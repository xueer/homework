#encoding:utf-8
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

iches = 2.54
lbs = 0.45359237
height = my_height * iches

weight = my_weight * lbs



puts -7 / 3
puts 7 / 3
puts 7 % 3
puts -7 % 3
puts 5 / 0.0
puts "Let's talk about %s." % my_name
puts "让我们 说关于 %s." % my_name  #如果说支持中文的话,在最前面加上#encoding:utf-8
puts "He's %d inches tall." % my_height
puts "He's %d pounds heavy." % my_weight
puts "Actually that's not too heavy."
puts "He's got %s eyes and %s hair." % [my_eyes, my_hair]
puts "His teeth are usually %s depending on the coffee." % my_teeth
puts "He's #{height} "
puts "He's #{weight} "
# this line is tricky, try to get it exactly right
puts "If I add %d, %d, and %d I get %d." % [
    my_age, my_height, my_weight, my_age + my_height + my_weight]
# %d 整型输出,%s以字符输出  %f  浮点数输出" %3d"  单引号也可以用
# puts= "%s%d" %['abc',123]
# irb 退出exit