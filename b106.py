n=int(input("enter the number"))
a=int(input("enter the number"))
l=[]
count=0
for i in range(n):
  s=int(input())
  l.append(s)
for i in l:
  if(i%2!=0):
    count=count+1
  if(count==a):
    print(i)
