sum = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    sum += number
print("The sum of all numbers is:", sum)