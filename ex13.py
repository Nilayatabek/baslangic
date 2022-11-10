for x1 in range(10,99):
    a=100*x1
    for x2 in range (10,99):
        b=a+x2
        if b==11*(x1+x2):
            print(x1,x2)
