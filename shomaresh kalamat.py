x=input("please entery a sentence:")
y=len(x)
print("Number of the character:",y)
e=x.count(".")+x.count("?")+x.count("!")+x.count(":")
print("Number of sentence:",e)
z=x.count(" ")
z=z +e
print("Number of words:",z)
