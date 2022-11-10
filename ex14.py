nile=[]
for x in range(1,1000000):
    x=x
    for b in range(1,1000000):
        b=b
        if x*b==121212 and x>b:
         a=x-b
         nile+=[a]
         c=min(nile)
         if x-b==c:
          print(x,b)
        
 
