n=int(input())
for i in range(0,n):  
    for j in range(0,n):
        if(i!=j and j!=n-1-i   ):
            print(j,end=' ') 
        else:
            print(end='  ')      
    print()
