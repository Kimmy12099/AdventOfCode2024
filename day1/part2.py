import pandas as pd 

df = pd.read_csv("part1.txt", header= None, sep="   ")

col1= df[0].tolist()
col2 = df[1].tolist()

# print(col1)
# print(col2)

col1.sort()
col2.sort()

similarities = 0

for i in range(len(col1)):
    count = 0
    for x in range(len(col2)):
        if col1[i] == col2[x]:
            count += 1 
    similarities += col1[i]*count 

print(similarities)
            

