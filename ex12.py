x=0

for b in range(1000,2005):
    x=0
    for i in str(b): 
      x+=int(i)
    if x==2005-b:
        print(b)
        
        
   
