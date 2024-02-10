rows = 5


for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)


for i in range(rows - 1, 0, -1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)