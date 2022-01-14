a=int(input())
b=2
while b<a:
    if(a%b==0):
        print("not prime Number")
        break
    b=b+1
else:
    print("prime Number")
