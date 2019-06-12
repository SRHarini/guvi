g=int(input())
if(g==2 or g==3):
  print("yes")
if(g>3):
  for i in range(2,10):
    if(g%i==0):
      c=0
      break
    else:
      c=1   
  if(c==0):
    print("no")
  else:
    print("yes")
  


