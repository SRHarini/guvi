get=int(input())
for i in range (0,get+1):
  k=2**i 
  if(get<k):
    print(k)
    break
