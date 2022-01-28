for i in range(7):
    for k in range(2):
        print(i*" ",end="")
        for j in range(6-i):
            print("*",end=" ")
        print(" "*i,end='')
    print()
