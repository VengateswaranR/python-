a=int(input("number from where to start: "))
r=int(input("divisible number which is closer: "))
c=[]
for i in range(a-r,a+r):
    if i%r==0:
        c.append(i)
d=c[0] if c[0]<c[1] else c[1]
print(d)
        
