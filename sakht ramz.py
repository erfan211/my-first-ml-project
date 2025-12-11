while True:
    x=input("yeki ro entekhab kon:\n1)ramz negar\n2)ramz khan\n3)khoroj")
    if x=="1":
        jom=input("jomle ro vared kon")
        r=""
        for i in jom:
            z=ord(i)*2+5
            r+=chr(z)
        print(r)
    elif x=="2":
        jom=input("jomle ro vared kon")
        r=""
        for i in jom:
            z=(ord(i)-5)//2
            r+=chr(z)
        print(r)
    else:
        break