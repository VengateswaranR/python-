n=int(input())
for i in range (4*n):
    for j in range(4*n):
        if i in [0,n-1,4*n-1,3*n] or j in [0,n-1,4*n-1,3*n]:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
