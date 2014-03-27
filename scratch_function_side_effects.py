# creating a user class
class User(object):
	"""docstring for User"""
	def __init__(self, name):
		self.num_list = [1,2,3]
		self.name_list = ['adrian','jason']
		self.name = name
		
	def introduce(self):
		print "My name is ", self.name
		print "My list is ", self.num_list
		print "My names are ", self.name_list

# defining a function that takes a string and object and 
# modify them locally
def change(tupled, object):
	tupled = [4,5,6]
	object.name = "another new name"
	object.num_list = (4,5,6)
	object.name_list = []

#creating our user and string
fred = User("fred")
bill = [1,2,3]

#showing current values
fred.introduce()
print bill

#calling the function that makes changes to them locally
change(bill, fred)

# showing their values after the change
fred.introduce()
print bill