k=int(input())
i,j=map(int,input().split())
for n in range(i+1,j):
  if(k==n):
    k=n+1
    print("yes")
    break
if(k==k+1 or k==i or k==j):
  print("no")
