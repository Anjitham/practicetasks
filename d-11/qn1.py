lst=[1,6,5,2,3,4]
if len(lst)<2:
    print("Not possible to find")
else:
    max_num=max(lst)
    lst.remove(max_num)
    
second_largest=max(lst)
print(f"second largest is {second_largest}")



