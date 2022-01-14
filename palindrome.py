a=int(input())
b=''
d=a
while a>0:
    c=a%10
    b=b+str(c)
    a=a//10
if d==int(b):
    print('palindrome')
else:
    print('not palindrome')
