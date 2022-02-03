n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        for j in range(0,n):
            if j!=0 and j<n//2 and (i==n-1 or i==0) or j==n-1 and i!=0:
                print("*",end =' ')
            else:
                print(" ",end=" ")
        print()
    else:
        for j in range(n):
            if j==0 or (j==n-1 or j==n//2) and i>n//2 or i==n//2 and j>=n//2:
                print("*",end =' ')
            else:
                print(" ",end =' ')
        print()
