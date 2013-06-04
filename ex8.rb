formatter = " %s %s %s %s"  #这个里面的前后客格,会影响到\n的效果,去掉空格或加空格会将第一行与第二行对齐

puts formatter % [1,2,3,4]
puts formatter % ["one","two","three","four"]
puts formatter % [true, false, false, true]
puts formatter % [formatter, formatter, formatter, formatter]
puts formatter % ["I had this thing.\n","That you could type up right.\n","But it didn't sing.\n","So I said goodnight."]


