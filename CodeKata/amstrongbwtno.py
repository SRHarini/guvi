i,j=map(int,input().split())
for n in range(i+1,j):
   k = len(str(n))
   add = 0
   t= n
   while t> 0:
       d = t% 10
       add+= d**k
       t //= 10
   if (n==add):
      print(n,end=" ")
