print('*********** Scientific Calculator**********')
print('Choose below options to perform operation')



x=True
while x :
    print(" Press 1 for Addition")
    print(" Press 2 for Subtraction")
    print(" Press 3 for Multiplication")
    print(" Press 4 for Division")
    print(" Press 5 for exit")
    a = input("Enter your first arg ")
    b = input("Enter your second arg ")
    choice = input("Enter your choice ")
    if(choice =='1'):
        sum=int(a)+int(b)
        print("sum is"),print(sum)
    elif(choice=='2'):
        diff=int(a)-int(b)
        print("diffrence is"),print(diff)
    elif(choice=='3'):
        mul=int(a)*int(b)
        print("product is"),print(mul)
    elif(choice=='4'):
        try:
            div=int(a)/int(b)
            print("product is"),print(div) 
        except ZeroDivisionError:
            print("exception handled")      
    else:
        print("Exiting from calculator...")
        break
