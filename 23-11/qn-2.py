n=int(input("Enter a number:"))

square=[]
cube=[]

for i in range(1,11):
    square.append(i**2)
    cube.append(i**3)

print(f"square list{square}")
print(f"cube list{cube}")