n=int(input())
for i in range(n):
    if i==0 :
        for j in range(0,n):
            print("*",end =' ')
    else:
        for j in range(0,n):
            if(j==n//2):
                print("*",end =' ')
            else:
                print(" ",end=" ")
    print()
