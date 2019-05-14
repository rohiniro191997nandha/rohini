s=input("enter the string")
len=len(s)
odd=[]
even=[]
z=[]
y=[]
str=""
str1=""
for i in range(len):
  if(i%2==0):
    even.append(i)
  else:
    odd.append(i)
for j in even:
  z.append(s[j])
for k in z:
  str=str+k
for r in odd:
  y.append(s[r])
for f in y:
  str1=str1+f
print(str,str1)
