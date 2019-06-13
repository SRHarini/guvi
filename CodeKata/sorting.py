j=int(input())
li=[]
li=map(int,input().split())
m=list(li)
m.sort()
if(len(m)==j):
  for i in m:
    print(i,end=" ")
