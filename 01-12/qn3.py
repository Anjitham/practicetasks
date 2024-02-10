
row=5
for i in range(row):
    asci=65
    for j in range(row-i-1):
        print("",end=" ")

    
    for k in range(i+1):
        print(chr(asci),end=" ")
        asci+=1
    print()
    
