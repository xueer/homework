#画出一个三角形
m=4
for i in range(0,5):
	for j in range(0,5):
		if j<m:
			print ' ',
		else:
			print '*',
		j +=1
	m -=1
	i +=1
	print "\n"
