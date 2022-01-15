n=int(input())
if(n%2==0):
    for i in range(0,n):  
        for j in range(1,n):
            if(j!=n//2 and i!=n//2):
                print(j,end=' ') 
            else:
                print(end='  ')      
        print()
else:
    for i in range(0,n):  
        for j in range(0,n):
            if(j!=n//2 and i!=n//2):
                print(j,end=' ') 
            else:
                print(end='  ')      
        print()
