num_list=[1,2,3,4,5] 
num_set=set()
for i in num_list:
    for k in num_list:
        for j in num_list:
            num=i*100+j*10+k 
            num_set. add (num)
print (num_set)