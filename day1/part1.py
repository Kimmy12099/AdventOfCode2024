import pandas as pd 

df = pd.read_csv("part1.txt", header= None, sep="   ")

col1= df[0].tolist()
col2 = df[1].tolist()

# print(col1)
# print(col2)

col1.sort()
col2.sort()

differences = []

for i in range(len(col1)):
    differences.append(abs(col1[i] - col2[i]))

print(sum(differences))
