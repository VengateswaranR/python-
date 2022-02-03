n=int(input())
for i in range(n):
    if i==0:
        for j in range(0,n):
             print("*",end =' ')
        print()
    elif i==n-1:
        for j in range(0,int(n//2)):
             print("*",end =' ')
        print()    
    else:
        for j in range(n):
            if j==n//2:
                print("*",end =' ')
            else:
                print(" ",end =' ')
        print() 
