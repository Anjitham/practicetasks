n1=int(input("Enter a n1:"))
n2=int(input("Enter a n2:"))
op=input("Enter operator:")
if op=="-":
    print(n1-n2 if n1>n2 else n2-n1)
elif op=="+":
    print(n1+n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
elif op=="%":
    print(n1%n2)
elif op=="//":
    print(n1//n2)
elif op=="**":
    print(n1**n2)
