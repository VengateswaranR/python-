b=input()  
c=b.split()
d=" "
for i in range(len(c)-1,-1,-1):
    d=d+c[i]+" "
print(d)
