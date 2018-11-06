# Python program to demonstrate  
# Creation of Set in Python 
  
# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 
  
# Creating a Set with  
# the use of a String 
set1 = set("RahulMeetsRahul") 
print("\nSet with the use of String: ") 
print(set1) 
  
# Creating a Set with 
# the use of Constructor 
# (Using object to Store String) 
String = 'RahulMeetsRahul'
set1 = set(String) 
print("\nSet with the use of an Object: " ) 
print(set1) 
  
# Creating a Set with 
# the use of a List 
set1 = set(["Rahul", "Meets", "Rahul"]) 
print("\nSet with the use of List: ") 
print(set1) 
  
# Creating a Set with  
# a List of Numbers 
# (Having duplicate values) 
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
print("\nSet with the use of Numbers: ") 
print(set1) 
  
# Creating a Set with  
# a mixed type of values 
# (Having numbers and strings) 
set1 = set([1, 2, 'Rahul', 4, 'Meets', 6, 'Rahul']) 
print("\nSet with the use of Mixed Values") 
print(set1) 