a=50
b=5000
c=0
d=[]
while a>=0:
    print("Enter the options you have to done:")
    print(" 1.Book\n 2.Cancel\n 3.print\n 4.Exit")
    n=int(input())
    if n==1:
        if a!=0:
            id=input("Flight Id:")   
            print("Number of seats available:{0}\nCurrent Ticket price for each seats:{1}".format(a,b))
            name=input("Enter the name:")
            aid=int(input("Enter Adhar number:"))
            c=int(input("Seat going to book:"))
            if c<=a:
                d.append(name)
                d.append(aid)
                d.append(id)
                d.append(c)
                d.append(b*c)
                print("seat booked by an passenger:{0}\nTotal cost:{1}".format(c,b*c))
                a=a-c
                b=b+(c*200)
                c=0
            else:
                 print("Sorry, Only {0} tickets are available".format(a))
        else:
             print("Booking Closed")
            
    elif n==2:
        aid=int(input("Enter the Adhar ID Number:"))
        if aid in d:
            e=d.index(aid)
            print("Details of the passenger")
            print("Passenger -> {0}\t aid -> {1}\n   Flight ID -> {2}\t Seats booked -> {3}\t Ticket Amount -> {4}".format(d[e-1],d[e],d[e+1],d[e+2],d[e+3]))
            print("To continue process 'y' or 'n'")
            f=input()
            if(f=='y'):
                    f=d[e+3]
                    b=b-(d[2+e]*200)
                    a=a+d[2+e]
                    for i in range(0,5):
                        d.remove(d[e-1])
                    print("Your tickets are cancelled")
                    print("Amount Refunded:",f)
            else:
                    print("Process Terminated")
        else:
             print("given Information was wrong")
    elif n==3:
        for i in range (0,int(len(d)/5)):
            print("Passenger -> {0}\t aid -> {1}\n   Flight ID -> {2}\t Seats booked -> {3}\t Ticket Amount -> {4}".format(d[0+5*i],d[1+5*i],d[2+5*i],d[3+5*i],d[4+5*i])) 
    elif(n==4):
        print("Welcome")
        break
    else:
        continue
