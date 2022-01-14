a=int(input())
c=0
d=a
while a!=0:
    b=a%10
    c=c+pow(b,3)
    a=a//10
if(c==d):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
