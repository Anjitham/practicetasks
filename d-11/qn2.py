ht={"arush":160,"akshath":170,"eva":165,"viam":145,"eva":176}
min_ht=170
res={name:height for name,height in ht.items() if height>=min_ht }
print(res)