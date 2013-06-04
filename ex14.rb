user = ARGV.first  #第一个参数传入user
prompt = '> '    #提示符大于号

puts "Hi #{user}, I'm the #{$0} script."  #当前脚本名称
puts "I'd like to ask you a few questions."
puts "Do you like me #{user}?"
print prompt
likes = STDIN.gets.chomp()     #表示从当前输入设备中取东西.如果gets.chomp()传参数了,gets会从文件里面取东西.

puts "Where do you live #{user}?"
print prompt
lives = STDIN.gets.chomp()

puts "What kind of computer do you have?"
print prompt
computer = STDIN.gets.chomp()

puts <<MESSAGE
Alright, so you said #{likes} about liking me.
You live in #{lives}.  Not sure where that is.
And you have a #{computer} computer.  Nice.
MESSAGE

