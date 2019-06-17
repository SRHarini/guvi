get=input()
alp=False
num=False
for i in get:
  if(i.isalpha()==True):
    alp=True
  if(i.isdigit()==True):
    num=True
if(alp==True and num==True):
  print("Yes")
else:
  print("No")
