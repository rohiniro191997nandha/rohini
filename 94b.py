n=int(input("enter the count"))
pos=int(input("enter the position"))
l=[]
for i in range(n):
  num=int(input())
  l.append(num)
element=l[pos-1]
print(element)
