b=input()
c=b.split()
e=""
d=""
for i in c:
    if c.index(i)%2!=0:
        for j in range(len(i)-1,-1,-1):
            d=d+i[j]
        e=e+d+" "
        d=""
    else:
        e=e+i+" "
print(e)
