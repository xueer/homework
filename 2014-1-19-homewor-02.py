#写一个猜数字游戏。每次随机1到100里面随机抽一个数，让用户输入，用户输入的比那个数大，就打印large，小的话就打印small，如果正确就提示用户，you win
num2 = random.randint(1,101)
#print num2

while True:
	num1 = int(raw_input("游戏开始,请输入所猜数字:"))
	if num1 > num2:
		print "The guess is large."
	elif num1 < num2:
		print "The guess is small."
	else:
	    print " You win."
	    break
print "游戏结束."
