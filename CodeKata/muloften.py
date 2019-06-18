get=int(input())
for i in range (10,get+10,10):
  k=i*1
  if(get<k):
    print("k",k)
    break
  else:
    i=(i+10)*1
    if(get<i):
      print(i)
      break
