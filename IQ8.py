a=int(input())
c=[]
for i in range(0,a):
    b=int(input())
    c.append(b)
for j in range(0,a):
    for k in range(j+1,a):
        if c[j]<c[k]:
            print(c[j],"->",c[k])
            break
    else:
        print(c[j],"-> -1")
