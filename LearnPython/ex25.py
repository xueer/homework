#coding=UTF-8
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')   #作用split按空格拆分字符串.
	return words
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def get_first_word(words):
	return words.pop(0)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	#word = words.pop(0)
	word = get_first_word(words)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)

	print word
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

assert break_words('this is a string') == ['this','is','a','string']
assert break_words('hello world') == ['hello','world']
assert 'hello world'.split(' ') == ['hello','world']



assert sort_sentence('this is a string') == ['a','this','is','string']

assert sort_words(['d','c','b','a']) == ['a','b','c','d']



assert get_first_word(['this','is']) == 'this'





# 格式的：

# 姓名，年龄|另外一个用户姓名，年龄

# name:haha,age:20|name:python,age:30|name:fef,age:55

# 那我们可以通过字符串对象的split方法切割字符串对象为列表。

# a = 'name:haha,age:20|name:python,age:30|name:fef,age:55'

# print a.split('|')

# 返回结果：

# ['name:haha,age:20', 'name:python,age:30', 'name:fef,age:55']

