#encoding:utf-8
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
puts "数组的长度为："+animals.size.to_s
puts animals
animals[0]='peacock'
animals[1]='whale'
animals[2]='bear'
animals[3]='platypus'
animals[6]='monkey'


puts "The 1st animal is at 0 and is a " +animals[0]
puts "The 2se animal is at 1 and is a " +animals[1]
puts "The 3rd animal is at 2 and is a " +animals[2]
puts "The 4fo animal is at 3 and is a " +animals[3]

puts animals.first
puts animals.last

puts "数组的长度为："+animals.size.to_s
puts "第二个元素为："+animals[1]
puts "最后一个元素为："+animals[-1]
