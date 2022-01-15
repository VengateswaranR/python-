n=int(input())
for i in range(0,n):  
    for j in range(0,n):
        if(j==n//2 or i==n//2):
            print(j,end=' ') 
        else:
            print(end='  ')      
    print()
