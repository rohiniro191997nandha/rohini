str=input("enter the string")
count=0
for s in str:
  if(s=="a" or s=="e" or s=="i" or s=="o" or s=="u" or s=="A" or s=="E" or s=="I" or s=="O" or s=="U"):
    count=count+1
if(count==0):
  print("no")
else:
  print("yes")
