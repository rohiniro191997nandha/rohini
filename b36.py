import re
s=input("enter the val")
specialchar=len(s)-len(re.findall('[\w]',s))
print(specialchar)
