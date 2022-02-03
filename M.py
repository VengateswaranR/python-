n=int(input())
for i in range(0,n):                         
    for j in range(0,n):              
        if(j==0 or j==n-1 or i<=n//2 and i==j or i<=n//2 and j==n-1-i):                
            print("*",end=' ')         
        else:            
            print(end='  ')          
    print()
