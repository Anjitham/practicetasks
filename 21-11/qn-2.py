num=int(input("Enter a decimal no:"))
binary=""
while num>0:
    remainder =num % 2
    binary = str(remainder) + binary
    num //= 2

print(f"Binary representation is {binary}")