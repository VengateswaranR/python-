b=input()  
c=input()
g=b.split()
h=c.split()
d= len(g) if len(g)<len(h)else len(h)   
e='' 
for i in range(0,d): 
     e=e+g[i]+" "+h[i]+" "  
f= len(g) if len(g)>len(h)else len(h) 
for i in range(d,f): 
    if len(h)-f>=0: 
        e=e+h[i]+" "
    else:
        e=e+g[i]+" "
print(e)
