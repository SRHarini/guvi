get = int(input())
string = str(get)
reverse=""
for x in string:
  reverse = x + reverse
if(string==reverse):
  print("yes")
else:
  print("no")
