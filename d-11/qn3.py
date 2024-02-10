num=4
for row in range(1,2*num):
    for col in range(1,2*num):
        print(max(row-3,col-3,2*num-row-3,2*num-col-3),end=" ")
    print()