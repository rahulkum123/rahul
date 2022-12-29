rows=7
for i in range(rows):
    for j in range(rows-1):
        print(" ",end="")
    for j in range(rows):
        if i==0 or i==rows-1:
            print("*",end="")


            0
          else:
            if i==j-1:
                print("*",end="")
            else:
                print("",end="")
    print()