
a= int(input())
p={}
for i in range(a):
    n=input("Enter the Name of employee: ")
    s=int(input("Enter the Salary of employee: "))
    p[n]=s
b=[]
for i,j in p.items():
    b.append(j)
print("Highest Salary: ",max(b))
print("Lowest Salary: ",min(b))
print("Total Salary: ",sum(b))
print("Average Salary: ",sum(b)/a)
c=[]
for i,j in p.items():
    if j not in c:
        c.append(j)
for i in sorted(c):
    print("Employee Detail who get Salary {0}".format(i))
    for j,k in p.items():
        if i==k:
            print(j)
d=input("Enter the Name of Employee weather present or not: ")
for i,j in p.items():
    if d==i:
        print("{0} is present and Salary of {0} is {1}".format(i,j))
        break #key has no duplication so confidentah break use panlam
else:
    print(d,"is not present")
e=int(input("Check the Salary is given or not: "))
if e in b:
    print("Yes")
    for j,k in p.items():
        if k==e:
            print(j)
else:
    print("No")
