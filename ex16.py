x=int(input())
if x>1:

  for i in range(2,x):
   if x%i==0:
    print("asal sayı değil")
    
   else:
    print("oldukça asal ve asil")

else:
    print(x, "asal sayı değildir")
