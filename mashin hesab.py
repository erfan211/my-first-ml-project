num1=float(input("Enter a number1: "))
car=input("Do you wanna do car ?")
num2=float(input("Enter a number2: "))
if car=="+":
    z=num1+num2
    print(z)
elif car=="-":
    z=num1-num2
    print(z)
elif car=="*":
    z=num1*num2
    print(z)
elif car=="/":
    z=num1/num2
    print(z)
else:
    print("This character is not supported...")