#coding=UTF-8
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
			"I don't want to get sued",
			"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
			"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#以下是V2.0代码
cities = {'CA': 'San Francisco', 'MI': 'Detroit',
                     'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention!
cities['_find'] = find_city

while True:
    print "State? (ENTER to quit)",
    state = raw_input("> ")

    if not state: break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print city_found
 

