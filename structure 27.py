n=int(input())
for i in range (n):
    for j in range(2*n):
        if j<=n-1-i or j>=n+i:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
