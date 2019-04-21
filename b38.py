a,b=[int(a) for a in input("before swapping").split()]
a=a^b
b=a^b
a=a^b
print("after swapping",a,b)
