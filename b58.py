x=int(input("enter the count"))
y=int(input("num"))
l=[]
count=0
for i in range(x):
  num=int(input("numbers"))
  l.append(num)
for m in l: 
  if(m==y):
    count=count+1
if(count==0):
  print("no")
else:
  print("yes")
  
