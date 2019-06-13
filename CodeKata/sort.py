i=int(input())
l=[]
l=map(int,input().split())
li=list(l)
li.sort()
if(len(li)==i):
  for j in li:
    print(j,end=" ")
