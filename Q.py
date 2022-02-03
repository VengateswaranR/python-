n=int(input())
for i in range(n):
    if i==0 or i==n//2:
        for j in range(0,n):
            if j!=0 and j<n:
                print("*",end =' ')
            else:
                print("",end =' ')
        print()
    else:
        for j in range(n):
            if i<n//2:
                if j==0 or j==n-1 :
                    print("*",end =' ')
                else:
                    print(" ",end =' ')
            else:
                if j==i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")                                    
        print() 
