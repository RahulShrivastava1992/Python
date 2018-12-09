class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def parentMethod():
        print("I amm in parent method")
class  Child(Parent):
    def __init__(self,name,age):
            super().__init__(name,age)
            self.name=name
            self.age=age
    def childMethod():   
        print("I am in child method")
def Main():
        parent=Parent("Milky",29)
        child=Child("Rahul",34)
        print("my name is "+str(child.name))
        print("my age is "+str(child.age))
        print("my age is "+str(parent.age))
if __name__=='__main__':
    Main()