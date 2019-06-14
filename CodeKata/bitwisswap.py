i,j=map(int,input().split())
i=i^j
j=i^j
i=i^j
print(i,j,end=" ")
