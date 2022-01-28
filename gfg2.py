a=int(input("First term: "))
r=int(input("Common Ratio: "))
n=int(input("nth term need to print: "))
for i in range(0,n-1):
    a=a*r
print("G.P of nth Series: ",a)
