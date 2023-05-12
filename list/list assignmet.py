# #1. sum of all the items in a list
# list=[1,2,3,4,5]
# y=0
# for x in list:
#     y=y+x
# print(y)
##**************************************************
# #2.multiplies all items in list
# list=[1,2,3,4,5]
# y=1
# for x in list:
#     y=y*x
# print(y)
##**************************************************
# #3.to get largest no. from list
# list=[1,2,3,4,5]
# y=list[0]
# for x in list:
#     if y<x:
#         y=x
# print(y)
#**************************************************
# #5.Write a Python program to count the number of strings where the string
# # length is 2 or more and the first and last character are same
# #  from a given list of strings.
# list=['abc','xyx','12121','def','dsd','sds']
# i=0
# for x in list:
#    if x[0]==x[-1]:
#      i=i+1
# print(i)
##**************************************************
# #7.program to remove duplicates from a list.
# list1=[10,20,20,33,30,40,30,40]
# for x in list1:
#     i=list1.count(x)
#     if i>1:
#         list1.remove(x)
#
# print(list1)
#**************************************************
# #8.Write a Python program to check a list is empty or not.
# list1=[1,2,3,4,5,6]
# #list1=[]
# x=0
# for y in list1:
#     x=x+1
# print("No.of items",x)
# if x==0:
#     print("list is empty")
# else:
#     print("list is non empty")

#*********************
# #9. Write a Python program to clone or copy a list.
# list=[5,6,7]
# list1=list.copy()
# print(list)
# print(list1)
#**************************************************
# #12. Write a Python program to print a specified list after removing
# # the 0th, 4th and 5th elements.
# list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list1.remove(list1[5])
# list1.remove(list1[4])
# list1.remove(list1[0])
# print(list1)
#
# # #**************************************************
# #14.Write a Python program to print the numbers of a specified list after
# #  removing even numbers from it.
# #list1=[1,5,4,6,4,2,3,1,4,8]
# list1=[1,2,3,4,5,6,7,8]
# for x in list1:
#     if x%2==0:
#        list1.remove(x)
# print(list1)
# # #**************************************************
# #15. Write a Python program to shuffle and print a specified list.
#
#
#
# #19. Write a Python program to get the difference between the two lists
# s1={1,2,3,4}
# s2={4,5,6,7,8}
# print(s1.difference (s2))
#
# #54. Write a Python program to concatenate elements of a list.
# list1=[1,2,3,4]
# list2=[4,5,6,7,8]
# list=list1+list2
# print(list)
#
# #56. Write a Python program to convert a string to a list.?????
#
# s1="hello"
# #l1=set(s1)
# #print(l1)
# list3=[]
# for x in s1:
#     list3.append(x)
# print(list3)

#46. Write a Python program to select the odd items of a list.
list1=[1,5,4,6,4,2,3,1,4,8]
#list1=[1,2,3,4,5,6,7,8]
list=[]
for x in list1:
    if x%2==0:
        x=x+1
    else:
        #print(x)
        list.append(x)
print(list)


#43. Write a Python program to split a list into different variables.
list1=[[1,5,4],[6,4,2],[3,1,4],[8]]
print(type(list1))