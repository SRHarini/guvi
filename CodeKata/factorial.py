get=int(input())
if(get==0):
  print("1")
else:
  mul=1
  for i in range(1,get+1):
    mul=mul*i
  print(mul)
