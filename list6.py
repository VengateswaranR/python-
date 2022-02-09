b=int(input())
c=[]  
for i in range(0,b):
    d=int(input())
    c.append(d)
e=0
f=0
for i in range(0,b):
    if i%2==0:
        e=e+c[i]
    else:
        f=f+c[i]
print("Even numbers: ",e)    
print("Odd numbers: ",f) 
