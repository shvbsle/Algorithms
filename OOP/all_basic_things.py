'''
Goal of this code is to have a very well defined basic flow wise exploration of python OOP concepts
'''

# what is a class declare one:

class Dog:
	def __init__(self):
		print("A dog object is initialized")

d = Dog()
del d
# Class inheritance

class Golden_Retriever(Dog):
	'\nclass of a dog type that is inherited from base class Dog'

	def __init__(self):
		# classname.__doc__ prints out the first line after the dog class
		print(Golden_Retriever.__doc__)
		print("\nover riding the base class! \n this is a golden retriever class! :) \n")

d = Golden_Retriever()
del d

# Attribute access and class variables

class Many_Objects:
	'\nThis class is to demonstrate the class variables'
	#this is the class variables
	count = 0

	#this is the hidden variables
	__hidden_var = 42

	def __init__(self):
		# The prime difference between class variable is that it is called by class_name.variable_name
		Many_Objects.count +=1
		# This is the local variable
		# This will create a copy of the count variable and then increment it
		self.count-=1
		print(Many_Objects.__doc__)

	def access_hidden(self):
		self.__hidden_var+=1
		print(self.__hidden_var)

d,e,f = Many_Objects(),Many_Objects(),Many_Objects()

print(Many_Objects.count)
try:
	print(Many_Objects.__hidden_var)
except:
	print("unalbe to access hidden variable")

d.access_hidden()

# Python3 exception handling and other fun stuff


# finally is always performed
try:
	invalid = 1/0
except:
	print(" 1/ 0 not allowed")
finally:
	print("do this anyways coz its in finally")


#Else is performed only if no exception found
try:
	invalid = 1/2
except Exception as e:
	print("very bad", e[0])
else:
	print("everything went well")


# this is a prime number generator class

class Prime:
	def __init__(self, limit):
		self.limit = limit
		self.found = 0
		self.start = 2

	# the __iter__ method is usually called by a for loop
	def __iter__(self):
		return self

	# the __next__ method is usually called when someone calls next() on an iterator instance of a class
	def __next__(self):
		if(self.found < self.limit):
			while not self.isprime(self.start):
				self.start+=1
			self.found+=1
		else:
			raise StopIteration
		return self.start-1

	# check if prime
	def isprime(self, n):
		for i in range(2, n):
			if n%i == 0:
				return False
		self.start+=1
		return True

#print first 26 primes
p_pen = Prime(26)
for i in p_pen:
	print(i, end = " ")
del p_pen
# generator example!:
def prime_generator(limit):
	p_pen = Prime(limit) # using this cos I dontwanna write isprime again
	num = 2
	for i in range(0, limit):
		while not p_pen.isprime(num):
			num+=1
		num+=1
		yield num-1

p_gen = prime_generator(26)
print(" \nhere is the same output generated using an generator ans is easier!!")
print("here is what happens by calling 'next(obj.__iter__()': ", next(p_gen), "\nand here is the normal for loop call:")
for i in p_gen:
	print(i, end = ' ')





