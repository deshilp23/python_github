#list functions
list1=[10,20,30]
print(list1)
#*********append*****************
list1.append(212)
list1.append([1,2,3])
print(list1)
#*********extend********************
list1 .extend([5,8,9])
print(list1)
#**********insert*******************
list1.insert(6,1)
print(list1)
#**********remove************************
list1.remove(1)
print(list1)
#******************pop**************
list1.pop(1)
print(list1)
#***********clear***************
# list1.clear()
# print(list1)
#********index******************
x=list1.index(30)
print(x)
#***************index************
list1=[10,20,30,40,20,20,80,90]
for i in range(len(list1)):
    if list1[i]==20:
        print(i)
#**********count****************
x=list1.count(20)
print(x)
s1="Hello"
#convert string to list by using list()
list2=list(s1)
print(list2)
x=list2.count('l')
print(x)
#********sort**********************
list1=[5,1,9,8,2,6,5,0,1]
print(list1)
#list1.sort()
list1.sort(reverse=True)
print(list1)
#sort string
list2=['aaaa','bb','ccc']
print(list2)
#list2.sort() by alphabetics
list2.sort(key=len)
print(list2)
#*********************with out using copy(overlap list)*************
list1=[1,2,3]
list2=list1
list2[0]=90
print(list1)
print(list2)
#*****************with using copy*************
list1=[1,2,3]
list2=list1.copy()
list2[0]=90
print(list1)
print(list2)
#***************concat**********
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)
#**************astric***************
list1=[1,2,3]
list2=list1*4
print(list2)
#***************list comprehension*******************
#without list comprehension
list1=[10,20,30,40,20,20,80,90]
list2=[]
for x in list1:
    list2.append(x*x)
print(list2)
#with list comprehension
list1=[10,20,30,40,20,20,80,90]
list3=[i*i for i in list1]
print(list3)
list5=[1,2,3,4,5,6,7,8]
list4=[i for i in list5 if i%2==0]
print(list4)