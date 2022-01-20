a=input()
b,c=[],[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
        c.append(a.count(a[i]))
print(b[c.index(max(c))],"=>",max(c))
