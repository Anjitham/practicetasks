n1=int(input("Enter a value for n1:"))
n2=int(input("Enter a value for n2:"))
sum=0
for i in range(n1,n2):
    if i%2==0:
        sum+=i
print(sum)
    