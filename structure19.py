n=int(input())
for i in range(1,n):
    print("  "*(n-1-i),end=' ')
    for j in range(0,2*i-1):
        if (i-1)-j>=0:
            print(((i-1)-j),end=' ')
        else:
            print(-((i-1)-j),end=' ')
    print() 
