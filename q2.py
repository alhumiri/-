def f1(n):
    for i in range(0,n):
        k=4
        while k>i:
            print(' ',end='')
            k=k-1
        j=5
        while j<=5+i:
            print(j,end='')
            j=j+1
        print('\n')    
        
f1(5)
