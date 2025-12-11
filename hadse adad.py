from random import randrange
x=randrange(1,100)
shmaresh=0
while shmaresh<11:
    adad=int(input("please Choose a number between 1 and 100:"))
    if adad==x:
        print("very good!!!")
        print("adad meshe:",x)
        break
    elif adad > x:
        print("The desired number is smaller.")
    else :
        print("The desired number is larger.")
    shmaresh+=1
    print(shmaresh)
if adad!=x:
    print("ohhhh natonesti")