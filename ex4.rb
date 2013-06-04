#encoding:utf-8
#定义变量cars 并赋初值
cars = 100  #
space_in_a_car = 4.0  #每台车4个人
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  #空车
cars_driven = drivers #能开的车
carpool_capacity = cars_driven * space_in_a_car #载客总数
average_passengers_per_car = passengers / cars_driven  #每台车平均能载多少人

puts "There are #{cars} cars available."  #有100辆车可用
puts "There are only #{drivers} drivers available." #30个司机可用
puts "There will be #{cars_not_driven} empty cars today." #今天有多少空车
puts "We can transport #{carpool_capacity} people today." #今天我们总共运输多少人.
puts "We have #{passengers} passengers to carpool today." #今天我们有多少乘客.
puts "We need to put about #{average_passengers_per_car} in each car." #在每辆车要放多少乘客.

puts "cars is %d" %cars
puts '引用变量值时一定要用双引号,不要用单引号'