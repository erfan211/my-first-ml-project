print("What do you want to convert?kilo or metr")
x=input("g or m:")
if x=="g":
    y=int(input("for g to kg->1 \nfor g to mg->2\n:"))
    if y==1:
        adad=float(input("Enter the number yourself:"))
        adad/=1000
        print(adad)
    else:
        adad=float(input("Enter the number yourself:"))
        adad*=1000
        print(adad)
elif x=="m":
    y=int(input("for m to cm->1\nfor m to mm->2\nfor m to km->3\n:"))
    if y==1:
        adad=float(input("Enter the number yourself:"))
        adad*=100
        print(adad)
    elif y==2:
        adad=float(input("Enter the number yourself:"))
        adad*=1000
        print(adad)
    else:
        adad=float(input("Enter the number yourself:"))
        adad/=1000
        print(adad)
else:
    print("The number entered is incorrect.")