arr=[1,-1,2,-3,4,5,-6,-7]
neg=[]
pos=[]
for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print(f"negative numbers are:{neg} and positive numbers are:{pos}")
