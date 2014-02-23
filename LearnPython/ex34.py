#coding=UTF-8
#序数ordinal==有序,以1开始;基数cardinal==随机选取,以0开始,序数-1==基数
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print 'The animal at 1 is the 2nd animal and is a ',animals[1] 
print 'The 3rd animal is at 2 and is a ',animals[3-1]
print 'The 1st animal is at 0 and is a ',animals[1-1]
print 'The animal at 3 is the 4th animal and is a ',animals[3]
print 'The 5th animal is at 4 and is a',animals[5-1]
print 'The animal at 2 is the 3rd animal and is a',animals[2]
print 'The 6th animal is at 5 and is a',animals[6-1]
print 'The animal at 4 is the 5th animal and is a',animals[4]
assert animals[5] == 'platypus'
assert animals[4] == 'whale'