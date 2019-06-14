get=int(input())
fst=0
snd=1
if(get==0):
  print(fst)
else:
  print(snd,end=" ")
  for i in range(1,get):
    cnt=fst+snd
    print(cnt,end=" ")
    fst=snd
    snd=cnt
