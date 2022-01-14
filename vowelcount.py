a=input()
b=0
c=0
while b<len(a):
    if(a[b] in ['a','e','u','i','o','A','E','I','O','U']):
        c=c+1
    b=b+1
print(c)

