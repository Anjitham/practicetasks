p1=int(input("Enter age of person 1:"))
p2=int(input("Enter age of person 2:"))
p3=int(input("Enter age of person 3:"))

if (p1>p2 and p1>p3):
    print(f"{p1} is Oldest")
    print(f"{p3} is youngest" if p2>p3 else f"{p2} is Youngest" )

elif (p2>p1 and p2>p3):
    print(f"{p2} is Oldest")
    print(f"{p3} is Youngest" if p1>p3 else f"{p1} is Youngest")


elif (p3>p1 and p3>p2):
    print(f"{p3}is Oldest")
    print(f"{p2} is Youngest" if p1>p2 else f"{p1} is Youngest")

elif (p1==p2 and p2==p3):
    print("All ages are same")