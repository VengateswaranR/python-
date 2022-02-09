b=input()
c=''
d=''
for i in range(0,len(b)):
    if b[i].isalpha():
        c=c+b[i]
    else:
        d=d+b[i]        
print(c)
print(d)
