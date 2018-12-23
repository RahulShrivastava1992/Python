# A Python program to demonstrate working of Generators 
def Reverse(data): 
	# this is like counting from 100 to 1 by taking one(-1) 
	# step backward. 
	for index in range(len(data)-1, -1, -1): 
		yield data[index] 

def Main(): 
	rev = Reverse('heloo python') 
	for char in rev: 
		print(char) 
	data ='heloo python Harssh'
	print(list(data[i] for i in range(len(data)-1, -1, -1))) 

if __name__=="__main__": 
	Main() 
