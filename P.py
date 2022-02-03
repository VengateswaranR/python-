n=int(input())
for i in range(n):
    if i==0  or i==n/2:
        for j in range(0,int(n/2)-1):
             print("* ",end =' ')
        print()
    else:
        for j in range(int(n/2)):
            if j==0 or j==int(n/2)-1 and i<=n//2:
                print("* ",end =' ')
            else:
                print("  ",end =' ')
        print() 
