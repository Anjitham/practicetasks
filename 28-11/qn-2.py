tup=(1,2,3,4,5)
lst=list(tup)
sum=0
for ele in lst:
    sum=sum+ele
    ele+=1
print(sum)