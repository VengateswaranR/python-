a=input()
d=a.lower()
b=''
c,e,f=[],[],[]
for i in range(0,len(d)):
    if d[i]!=" ":
        b=b+d[i]
    else:
        c.append(b)
        b=''
for j in range(0,len(c)):
    if c[j] not in e:
        e.append(c[j])
        f.append(c.count(c[j]))
print(e[f.index(max(f))],"=>",max(f))

