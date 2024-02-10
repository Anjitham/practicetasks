ascii_code = 65  # ASCII code for 'A'

for row in range(1, 6):
    for space in range(row, 5):
        print(" ", end="")
    for col in range(1,row+1):
        print(chr(ascii_code), end=" ")
        ascii_code += 1
    print()