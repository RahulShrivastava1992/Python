class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 0
	
	# A member method that changes 
	# __hiddenVariable 
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

# Driver code 
myObject = MyClass()	 
myObject.add(2) 
myObject.add(5) 

# This line causes error 
#print (myObject.__hiddenVariable) 
# This line will not causes error
myObject._MyClass__hiddenVariable=myObject._MyClass__hiddenVariable+2
print (myObject._MyClass__hiddenVariable)
