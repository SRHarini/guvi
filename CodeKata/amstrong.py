get=int(input())
st=list(str(get))
for i in range(0, len(st)): 
  st[i] = int(st[i])
val=0
for i in range(0,len(st)):
  val=st[i]**3+val
if(val==get):
  print("yes")
else:
  print("no")
