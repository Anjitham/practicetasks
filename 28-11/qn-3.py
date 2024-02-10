ascii=65
for row in range(1,6):
    for col in range(1,row+1):
        char=chr(ascii)
        print(char,end=" ")
    ascii+=1
    print()