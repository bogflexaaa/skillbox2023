a = int(input())

matrix = [[j+1 for j in range(a)] for i in range(a)]
for str in matrix:
    print(str)

for i in range(a):
    for j in range(i, a):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
for str in matrix:
    print(str)