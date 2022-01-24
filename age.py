import datetime
a=[]
e=datetime.datetime.now()
f=int(input("Enter the Year of Birth: "))
g=int(input("Enter the Month of Birth: "))
h=int(input("Enter the date of Birth: "))
b=e.year-f
c=e.month-g
d=e.day-h
if c>=0:
    print("{0} Years, {1} Months, {2} Day".format(b,c,d))
else:
    print("{0} Years, {1} Months, {2} Day".format(b-1,12+c,d))
    
