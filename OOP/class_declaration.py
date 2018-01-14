'''
This is the python code for class declarations and some certain class 
related functions 
'''

# in python, the class is initialized by __init__ function
# local variables are accessed by self.variable_name
# member functions are also accessed the same way

class Parent:
	local_variable = 0
	def __init__(self):
		print("parent initialized")

	def member_function(self, a, b):
		return a+b

	def access_variable(self,b):
		self.local_variable = b;
		print(self.local_variable)

p = Parent()
print(p.member_function(1,6))
p.access_variable(7)