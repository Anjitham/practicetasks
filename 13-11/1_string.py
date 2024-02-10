str=input("Enter a string:")
num=0
alpha=0
for ch in str:
    if ch.isalpha():
        alpha+=1
    elif ch.isalnum():
        num+=1
print(f"Alphabet count is{alpha}")
print(f"number count is{num}")