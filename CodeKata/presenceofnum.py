i,j=map(int,input().split())
k=list(input().split())
count=0
if(len(k)==i):
  for n in k:
    if(int(n)==j):
      count=1
  if(count==1):
    print("yes")
  else:
    print("no")
  
