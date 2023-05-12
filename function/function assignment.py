#1. Write a Python function to find the Max of three numbers.
def max(x,y,z):
    if x>y and x>z:
        print("x is max=",x)
    else:
        if y>x and y>z:
           print("y is max=",y)
        else:
            print("z is max=",z)
max(2,4,8)
max(34,6,23)

#2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
