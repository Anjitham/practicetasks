lower=int(input("Enter a number:"))
upper=int(input("Enter a number:"))

valid=True

n=int(input("Enter a number:"))
while valid==True:
    if lower<=n<=upper:
        print(f"{n} is in the range")
        break
    else:
        n=int(input("Enter the correct number:"))
       
    
