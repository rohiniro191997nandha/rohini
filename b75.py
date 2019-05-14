n=input("enter the string")
lst=list(n)
b=len(n)
str=""
if(b%2!=0):
  x=b//2
  y=round(x)
  lst[y]="*"
else:
  m=b//2
  a=m-1
  for c in range(a,m+1):
    lst[c]="*"
  for i in lst:
    str=str+i
  print(str)  
