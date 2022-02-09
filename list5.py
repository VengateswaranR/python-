b=int(input())
c=[]  
for i in range(0,b):
    d=int(input())
    c.append(d)
e=[]
for i in range(0,b-2):
    if c[i]==c[i+1] and c[i]==c[i+2]:
        e.append(c[i])
print(e) 
