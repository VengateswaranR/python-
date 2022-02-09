b=input()
c=''
for i in range(len(b)):
    if i%2!=0:
        for j in range(0,int(b[i])):
            c=c+b[i-1]
    else:
        c=c+b[i]
print(c)
