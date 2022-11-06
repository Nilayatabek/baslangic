liste=[0,1,2,3,4,5,6,7,8,9]
z=0
t=0
for a in liste:
    for b in liste:
        for c in liste:
            if a!=0 and c%2==0:
                if a==b or a==c or b==c:
                    print(a,b,c)
                    z+=1
                if a==b==c:
                    print(a,b,c)
                    t+=1
                    

print(z+t)                     
                    
                    
