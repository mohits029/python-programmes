s= 112544458
digit= set()

while True:
  
  if(s==0):
    break
  else:
   lastdigit= s%10
   digit.add(lastdigit)
   s= s//10

print(digit)
