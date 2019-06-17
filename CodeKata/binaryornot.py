get=int(input())
k=str(get)
cnt=0
for i in range(0,len(k)):
  if(k[i]=='0' or k[i]=='1'):
    cnt=1
  else:
    cnt=0
    break
if(cnt==1):
  print("yes")
else:
  print("no")
