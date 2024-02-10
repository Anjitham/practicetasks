p=float(input("Enter the principal amount:"))
r=float(input("Enter the interest rate:"))
t=float(input("Enter the no of year:"))

amount=p*(1+(r/100))**t
print(amount)
compound_interest=amount-p
print(compound_interest)
