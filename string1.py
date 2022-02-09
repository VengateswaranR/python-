b=input()  
c=input()
d= len(b) if len(b)<len(c)else len(c)   
e='' 
for i in range(0,d): 
     e=e+b[i]+c[i]   
f= len(b) if len(b)>len(c)else len(c) 
for i in range(d,f): 
    if len(c)-f>=0: 
        e=e+c[i] 
    else:
        e=e+b[i] 
print(e)
