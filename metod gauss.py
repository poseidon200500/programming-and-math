
def sorting(matrix):#сортировка матрицы по количеству главенствующих нулей(ступенчатый вид)
    k = len(matrix)
    for i in range(len(matrix)):
        countr = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                countr+=1
            else:
                matrix[i].append(countr)
                break
        if len(matrix[i]) == k:
            matrix[i].append(k+1)
    matrix.sort(key = lambda x: x[k])
    
    for i in range(len(matrix)):
        del matrix[i][-1]
    
    return matrix
def draw(matrix):
    print("==================")
    for i in range(len(matrix)):
        print(*matrix[i])
    print("==================")
#переменная axis принимает значения "gor" и "vert"
#три элементарных преобразования
def perestan(matrix,x,y,axis):#перестановка строк или столбцов 
    if axis == "gor":
        matrix[x],matrix[y] = matrix[y],matrix[x]
    else:
        for ind in range(len(matrix)):
            matrix[ind][x],matrix[ind][y] = matrix[ind][y],matrix[ind][x]
    
    return matrix
def multiplication(matrix,ind,koef,axis):# умножение строки или столбца на число
    if axis == "gor":
        for i in range(len(matrix[ind])):
            matrix[ind][i] *= koef
    else:
        for i in range(len(matrix)):
            matrix[i][ind] *= koef
    return matrix
def increase(matrix,x,y,koef,axis):#прибавление к одной строке другую помноженную на коэффициент у
    #x - главная строка, у - которую прибавляют
    if axis == "gor":
        for i in range(len(matrix[x])):
            matrix[x][i] += koef * matrix[y][i]
    else:
        for i in range(len(matrix)):
            matrix[i][x] += koef * matrix[i][y]
    return matrix
def perevod(matrix):
     
    glavx = 0 # место главы строки(столбец)
    glavy = 0 # главная строка, по которой проходит обнуление ряда(строка)
    for glavy in range(len(matrix)-1):
        #1)найти индекс главы строки
        for i in range(len(matrix[glavy])):
            if matrix[glavy][i] != 0:
                glavx = i
                break
        #2)умножить строку на 1/глава, чтобы глава стал равен 1
        print("ymn = ",glavx,matrix[glavy][glavx],1/matrix[glavy][glavx])
        matrix = multiplication(matrix,glavx,1/matrix[glavy][glavx],"gor")
        #3)обнулить столбец главы(кроме него), прибавив к каждой строке ниже главы строку главы умноженную на -1* элемент стоящий под главой
        for i in range(glavy+1,len(matrix)):
            matrix = increase(matrix,i,glavy,-1*matrix[i][glavx],"gor")    
    return matrix
        

#сделать переход к ступенчатой матрице и возможно к улучшеному виду

matrix = []
#=======================ввод
a = int(input())
for i in range(a):
    matrix.append(list(map(int,input().split())))
#=======================основное тело
matrix = sorting(matrix)
draw(matrix)
matrix = perevod(matrix)
#=======================вывод матрицы
draw(matrix)


