n=int(input())
for i in range (n):
    for j in range(2*n+1):
        if i<n//2 and (j<=n-1-i or j>=n+i):
            print("*",end=" ")
        elif i>n//2 and i%2==0 and (j>=n+i or j<=n-i) or j<=n-1-i or j>=n+1+i :
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
