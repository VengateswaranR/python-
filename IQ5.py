a=input()
d=a.lower()
b,c=[],[]
for i in range(0,len(d)):
    if d[i] not in b and d[i]!=" ":
        b.append(d[i])
        c.append(d.count(d[i]))
print(b[c.index(max(c))],"=>",max(c))
