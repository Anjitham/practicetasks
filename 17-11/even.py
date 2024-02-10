start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]

print("Original list of even numbers:", even_numbers)


even_numbers = [num for num in even_numbers if num % 5 != 0]


print("List of even numbers without multiples of 5:", even_numbers)