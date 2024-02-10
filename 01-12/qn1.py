input_list=[1,3,5,1,3,2,5,4,2] 
element_list=[] 
matrix_list=[]
count=0 
for i in input_list: 
    if i not in element_list: 
        element_list.append (i) 
        for i in element_list: 
            if input_list. count (i)==2:
                 matrix_list. append (list()) 
                 matrix_list[count].append(i) 
                 matrix_list[count].append(i) 
                 count=count+1 
            elif input_list. count(i)==1:
                 matrix_list.append(list())
                 matrix_list[count].append(i)
                 count=count+1 
matrix_list.sort() 
print(matrix_list)