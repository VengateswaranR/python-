n=int(input())
for i in range(0,n):  
    for j in range(0,n):
        if(i==j or j==0 or i==n-1 or j==n-1-i or i==0 or j==n-1):
            print(j,end=' ') 
        else:
            print(end='  ')      
    print()
