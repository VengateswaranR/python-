n=int(input())
b=""
a,c=0,0
while n>0:
    n=n/2
    if n.is_integer() :
        b='0'+b
    else:
        b="1"+b
        n=int(n)
for i in range(0,len(b)):
    if b[i]=='0':
        c=c+1
    else:
        a=a+1
print("Number of 0's in given decimal number:",c)
print("Number of 1's in given decimal number:",a)
