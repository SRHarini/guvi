h=input()
count=0
for i in h:
  if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
    print("yes")
    break
  else:
    count=count+1
if(count==len(h)):
  print("no")
