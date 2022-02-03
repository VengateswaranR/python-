import math
n=int(input())
for i in range(n):
    if i==0 or i==n-1 or i==n//2:
        for j in range(0,math.ceil(n/2)):
             print("* ",end =' ')
        print()
    else:
        for j in range(n):
            if j==0 :
                print("* ",end =' ')
            else:
                print("  ",end =' ')
        print() 
