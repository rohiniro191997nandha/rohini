x,y=[int(x) for x in input("enter a intervel").split()]
for num in range(x,y+1):
    if num>1:
      for i in range(2,num):
        if(num%i)==0:
          break
      else:
        print(num)
       
        
      
