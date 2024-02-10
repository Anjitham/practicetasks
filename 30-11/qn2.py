
input = input("Enter a string: ")


is_palindrome = True

start = 0
end = len(input) - 1

while start < end:
    if input[start] != input[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1


if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
