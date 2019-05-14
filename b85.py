s=input("enter the string")
len=len(s)
odd=[]
even=[]
for i in range(len):
  if(i%2==0):
    even.append(i)
  else:
    odd.append(i)
for j in even:
  print("even",s[j])
for r in odd:
  print("odd",s[r])
print("hai")
