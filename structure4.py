n=int(input())
for j in range(n,0,-1):  
    for i in range(1,n+1):
        if(i>=j):
            print(i,end=' ')
        else:
             print(end='  ')
    print()

