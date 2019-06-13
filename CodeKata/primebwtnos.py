i,j=map(int,input().split())
for k in range(i+1,j):
  if(k>1):
      for n in range(2,k):
        if(k%n)==0:
          break
      else:
        print(k,end=" ")
        

  
  
