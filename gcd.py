a=int(input())
b=int(input())
c=a if a>b else b
d=1
while d<c:
    if a%d==0 and b%d==0:
        e=d       
    d=d+1   
print(e)     


