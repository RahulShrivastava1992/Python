class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def parentMethod(self,name,age):
        print("I am in parent method"+name)
class  Child(Parent):
    def __init__(self,name,age):
            super().__init__(name,age)
            self.name=name
            self.age=age
    def childMethod(self,name,age):   
        print("I am in child method"+age)
def Main():
        parent=Parent("Milky",29)
        child=Child("Rahul",34)
        print("My name is "+str(child.name))
        print("My age is "+str(child.age))
        print("My name is "+str(parent.name))
        print("My age is "+str(parent.age))
if __name__=='__main__':
    Main()