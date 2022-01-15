n=int(input())
for i in range(0,n):  
    for j in range(0,n):
        if(i==j or j==n-1 or j==0):
            print(j,end=' ') 
        else:
            print(end='  ')      
    print()
