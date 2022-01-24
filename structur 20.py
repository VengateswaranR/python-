for i in range(1,6):
    print("  "*(5-i),end=' ')
    for j in range(0,2*i-1):
        print(chr(65+j),end=' ')
    print()
