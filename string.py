b=input()
c=0
for i in range(0,len(b)):
    if b[i].isdigit():
        c=c+int(b[i])      
print(c)
