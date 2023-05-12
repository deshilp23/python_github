s1='this is string'
s2="this is string"
s3="""this is string
this is string
this is string"""
print(type(s1))
print(type(s2))
print(type(s3))

#with interpoletion
fname="abc"
age=13
s1=f"hello {fname}.your age is {age}"
print(s1)

#accessing string
s1="hello world"
print(s1[0])
print(s1[-1])
print(s1[2:7:1])
print(s1[ : : ])
print(s1[ : :-1])

#capi,lower,upper,swapcase,title
s1="this IS DEMO STRING"
# print(s1)
# s2=s1.capitalize()
# print(s2)
# print(s1)
print(s1.lower())
print(s1.upper())
print(s1.swapcase())
print(s1.title())

#count, end with, start with

