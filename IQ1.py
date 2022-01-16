n=input()
b=''
for i in range((len(n)-1),0,-1):
    b=b+n[i]
b=b+n[0]
if(n==b):
    print("Palindrome")
else:
    print("Not Palindrome")
    
