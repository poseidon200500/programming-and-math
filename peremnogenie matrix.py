#Работает корректно
#а - строки, b - столбцы, перемножать матрицы можно только если a2 = b1
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
matrix1 = []
for i in range(a1):
    matrix1.append(list(map(int,input().split())))
matrix2 = []
for i in range(a2):
    matrix2.append(list(map(int,input().split())))
multimatrix = [[0 for i in range(b2)] for j in range(a1)]

for i in range(a1):
    for j in range(b2):
        summ = 0
        for k in range(len(matrix1[i])):
            summ+=matrix1[i][k] * matrix2[k][j]
        multimatrix[i][j] = summ

for i in range(len(multimatrix)):
    print(multimatrix[i])
