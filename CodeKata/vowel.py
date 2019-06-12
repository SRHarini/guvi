i=input()
l=len(i)
if(i.isalpha()==True and l==1):
  if(i=='a' or i=='A' or i=='e' or i=='E'or i=='i'or i=='I' or i=='o' or i=='O'  or i=='u' or i=='U'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
