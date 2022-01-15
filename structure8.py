n=int(input())
for i in range(0,n):  
    for j in range(0,n):
        if(j==i or j==n-i-1):
            print(j,end=' ') 
        else:
            print(end='  ')      
    print()
