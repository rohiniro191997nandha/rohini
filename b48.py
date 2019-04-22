lst=[]
num=int(input("how many numbers"))
for n in range(num):
  numbers=int(input("enter number"))
  lst.append(numbers)
s=sum(lst)
average=s/num
print(average)
