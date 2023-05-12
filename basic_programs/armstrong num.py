#find armstrong no. or not
a=int(input('Enter 3 digit number'))
b=a//100
c=a%100
d=c//10
e=c%10
f=b**3+d**3+e**3
if a==f:
    print("Armstrong number")
else:
    print("Not Armstrong number")
