

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    for col in range(row-1,0,-1):
        print(col,end=" ")
    print()
    