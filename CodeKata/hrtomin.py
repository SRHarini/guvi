mi=int(input())
if(mi<=59):
  print("0",mi)
else:
  h=mi//60
  m=mi%60
  print(h,m)
