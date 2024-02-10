
num=int(input("Enter a num:"))
factorial=1
is_prime=True #prime
for i in range(2,num,1):
    if (num%i==0):
        is_prime=False #not prime
        break
print(is_prime)
if is_prime==True:
    for i in range(1,num+1):
        factorial=factorial*i
print(f"the value is {factorial}")

