for i in  range(4,0,-1):
    for j in range(5-i):
        print(i,end=" ")
    print(" ",end="")
    if i!=1:
        for k in range(2*(5-i)+1):
            print("*",end=" ")
        print()
