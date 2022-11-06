liste=[0,1,2,3,4,5,6,7,8,9]
for a in liste:
    if 0<a<9:
        print(a,end=" ")
        
for b in liste:
    for c in liste:
     if b!=0 and c+b<9:
        print(b,c)
        
        
for d in liste:
    for e in liste:
        for f in liste:
          if d!=0 and d+e+f<9:
           print(d,e,f)
           


