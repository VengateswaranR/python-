b=input()
c=[]
for i in range(0,len(b)):
     if b[i] not in c:
        c.append(b[i])
print(c)
