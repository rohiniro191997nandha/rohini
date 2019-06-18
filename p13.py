import math
n=int(input())
rev=0
while(n>0):
  rem=n%10
  rev=rev+pow(rem,2)
  n=n//10
print(rev)  
