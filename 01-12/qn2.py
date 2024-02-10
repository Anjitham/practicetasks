no_unit_consumed=int(input("Enter units consumed:"))

if no_unit_consumed<=100:
    unit_rate=0
    bill=no_unit_consumed*unit_rate
elif no_unit_consumed<200:
    unit_rate=5
    bill=(no_unit_consumed-100)*unit_rate
elif no_unit_consumed>=200:
    unit_rate=10
    bill=100*5+(no_unit_consumed-200)*unit_rate

print(f"The bill amount is{bill}")