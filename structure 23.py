for i in range(7):
    for k in range(2):
        print((6-i)*" ",end="")
        for j in range(i):
            print("*",end=" ")
        print(" "*(6-i),end='')
    print()
