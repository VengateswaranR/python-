a=input()
b=''
c=len(a)
while c>0:
    b=b+a[c-1]
    c=c-1
if b==a:
    print('palindrome')
else:
    print('not palindrome')
