ht_in_cm=int(input("Enter ht in cm:"))
wt_in_kg=int(input("Enter wt in kg:"))

ht_in_m=ht_in_cm/100

bmi=wt_in_kg/(ht_in_m**2)
print(bmi)

if bmi<=19:
    print("0under weight")
elif bmi<25:
    print("You are healthy")
elif bmi<30:
    print("You are over weight")
else:
    print("You are obese")