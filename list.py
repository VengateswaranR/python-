l=[10,20,30,10,20,30,10,20,30,40,50,60]
a=[]
b=[]
for i in l:
    if i not in a:
        b.append(l.count(i))
        a.append(i)
for i in range(len(a)):
    print(a[i],"-->",b[i]
