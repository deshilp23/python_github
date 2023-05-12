#divisible by 7 and multiple of 5, between 1500 and 2700  (both included).
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print("no.divisible by 7 anf muliple of 5:",i)


#Write a Python program to construct  pattern, using a nested for loop.
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

#program to print alphabet pattern 'A
for i in range(1,7):
    for j in range(1,7):
        if j==1 or j==6 or i==3 :
           print("*",end='')
        else:
            print(" ",end='')
    print()
















