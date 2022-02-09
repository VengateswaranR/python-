n=int(input())
for i in range (n):
    for j in range(n):
        if i%2==0 and  j>=n-3-i or j>=n-2-i:
            print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()
