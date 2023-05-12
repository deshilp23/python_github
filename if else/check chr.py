# take char. input from user
ch=input("enter any single charecter or digit")
#convert char into ASCII
x=ord(ch)
if x>=65 and x<=90:
    print("capital")
elif x>=97 and x<=122:
    print("small case")
elif x>=48 and x<=57:
    print("digit")
else:
    print("I don't kown this charecter")