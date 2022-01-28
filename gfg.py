n= int(input())
b,c="",""
for i in range(0,n):
    b=b+str(i+1)
d=len(b)
for j in range(n,0,-1):
    for k in range(n*j,0,-1):
        if k%j!=0:
            c=c+b[d]
        else:
            d=d-1
            c=c+b[d]
    print(c)
    c=""
    d=len(b)
