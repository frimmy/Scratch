class Fish(object):
	def __init__(self, fish_name, color):
		self.name = fish_name
		self.color = color
		print "Fish init!"

	breathes_in_water = True
	skin = "scales"

class Goldfish(Fish):
	"""Goldfish class extending the Fish class"""
	def move(self, speed):
		print "Moving {}".format(speed)