n=input()
b=''
for i in range(0,len(n)):
    if i%2!=0:
        for j in range(0,int(n[i])):
            b=b+n[i-1]
print(b)       
