import math
path = r'data.txt'
final = []
for line in open(path,'r'):
    temp = (line.strip().split())
    for i in temp:
        final.append(i) ## mapping 
print(final)
temp_dict = dict()
for  i in range(len(final)):
    temp_dict[final[i]] =0 # mapping done
print(temp_dict)

for  i in range(len(final)):
    if(final[i] in temp_dict):
        temp_dict[final[i]] +=1 # 
print(temp_dict) # reducing done

for i,j in temp_dict.items():
    print(i,j)








