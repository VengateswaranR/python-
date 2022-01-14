a=int(input())
b=int(input())
c=a if a>b else b
while c>0:
    if c%a==0 and c%b==0:
        print(c)
        break
    c=c+1        


