import datetime
a=[]
e=datetime.datetime.now()
f=input("Enter Date of Birth(DD-MM-YYYY): ")
g=f.split("-")
b=e.year-int(g[2])
c=e.month-int(g[1])
d=e.day-int(g[0])
if c>=0 and d>=0:
    print("{0} Years, {1} Months, {2} Day".format(b,c,d))
elif c<0 and d>=0:
    print("{0} Years, {1} Months, {2} Day".format(b-1,12+c,d))
elif c<0 and d<0:
    print("{0} Years, {1} Months, {2} Day".format(b-1,c+11,d+31))
else:
    print("{0} Years, {1} Months, {2} Day".format(b,c-1,d+31))
