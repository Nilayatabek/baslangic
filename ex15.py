sayac=0
for j in range(10000,100000):
    sayac=0
    for i in range(2,j):
        if j%i==0:
            sayac+=1
    if sayac==0:
        print(j)
            

         
         
         
            
    

