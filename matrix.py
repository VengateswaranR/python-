b=[[10,20,30],[40,50,60],[70,80,90]]
c=[]
d=[]
for r in range(len(b)):
    for i in range(len(b[r])):
        if i==r:
            c.append(b[i][r])
        else:
            c.append(b[i][r])
    d.append(c)
    c=[]
print(d)
