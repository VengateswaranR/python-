a=input()
b,c=[],[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
        c.append(a.count(a[i]))
for j in range(0,len(c)):
    print(b[j],"=>",c[j])
