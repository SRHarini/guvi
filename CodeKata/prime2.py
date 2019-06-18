h = int(input())  
if (h > 1):  
   for n in range(2,h):  
       if (h % n) == 0:  
           print("no")  
           break
   else:  
       print("yes")  
else:  
   print("no")
