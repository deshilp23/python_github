#*****by zero based indexing***************
list1=[10,20,30,40,50,60,70,80,90,100]
#find size of list
print(len(list1))
#Access item by index
print(list1[2])
print(list1[len(list1)-1])
#for using for loop & index
for i in range(0,len(list1)):
    print(list1[i])
for i in range (len(list1)):
    print(list1[i])
#by using for each
for x in list1:
    #print(x)
    print(x*x)