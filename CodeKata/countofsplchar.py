get=input()
count=0
for i in get:
  if(i.isspace()==False and i.isnumeric()==False and i.isalpha()==False):
    count=count+1
print(count)
