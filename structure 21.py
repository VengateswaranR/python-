for i in range(0,16):
    if i<8:
        for k in range(7,i,-1):
            print(" ",end=' ')
        for j in range(i,-1,-1):
            if(i!=j):
                print(' ',end=' ')
            else:
                print('#',end=' ')
        for j in range(1,i+1):
            if(i!=j):
                print(' ',end=' ')
            else:
                print('#',end=' ')
    else:
        for j in range(0,8):
            if i-7!=j:
                print(' ',end=' ')
            else:
                print('#',end=' ')
        for j in range(5,-1,-1):
            if(i-8!=j):
                print(' ',end=' ')
            else:
                print('#',end=' ')
    print()
