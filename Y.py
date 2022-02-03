n=int(input())
for i in range(0,n):                         
    for j in range(0,n):              
        if(i==j and i<=n//2 or j==n-1-i):                
            print("*",end=' ')         
        else:            
            print(end='  ')          
    print()
