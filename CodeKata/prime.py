get = int(input())  
if (get > 1):  
   for i in range(2,get):  
       if (get % i) == 0:  
           print("no")  
           break
   else:  
       print("yes")  
else:  
   print("no")
