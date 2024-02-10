prev=0
curr=1

print(f"{prev},{curr}", end=",")

for i in range(1,11):
    next=prev+curr
    prev=curr
    curr=next
   
    print(next,"odd" if next%2!=0 else "even",end=" ")

