
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
            matrix[i].append(0)
    matrix.sort(key = lambda x: x[-1])
    
    for i in range(len(matrix)):
        del matrix[i][-1]
    
    return matrix
def draw(matrix):
    print("==================")
    for i in range(len(matrix)):
        print(*matrix[i])
    print("==================")
def gotoint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != int(matrix[i][j]):
                return matrix
    
    for i in range(len(matrix)):
        matrix[i] = map(int,matrix[i])
    return matrix
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

def opred2(m): #матрица только 2 на 2!
    return (m[0][0]*m[1][1] - m[0][1]*m[1][0])
def opred3(m): #матрица только 3 на 3 !
    return ((m[0][0]*m[1][1]*m[2][2]) + (m[1][0]*m[2][1]+m[0][2]) + (m[0][1]*m[1][2]*m[2][0]) -
            (m[0][2]*m[1][1]*m[2][0]) - (m[0][0]*m[1][2]*m[2][1]) - (m[0][1]*m[1][0]*m[2][2]) 
           )
def opredn(m): #матрица n-го порядка (не реализована) n > 3
    
    for i in range(len(matrix)):
        pass
        
def rang(matrix):    #определяет ранг матрицы (закончить)
    rang = 0
    flag = 0
    podmatrix = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            podm = [[matrix[i][j],matrix[i+1][j]],[matrix[i+1][j],matrix[i+1][j+1]]]
            if opred2(podm) != 0:
                rang = 2
                flag = 1
                podmatrix = podm
                if i != 0:
                    matrix = perestan(matrix,0,i,"gor")
                    matrix = perestan(matrix,1,i+1,"gor")
                if j != 0:
                    matrix = perestan(matrix,0,j,"vert")
                    matrix = perestan(matrix,1,j+1,"vert")
                break
        if flag == 1:
            break
    if flag == 0:
        for i in range(len(matrix)):
            if sum(matrix[i]) != 0:
                flag = 1
                break
    else:
        for i in range(min(len(matrix), len(matrix[0]))):
            pass #вот тут доделать
    
    return rang
def perevod(matrix): #работает некорректно, надо исправить
     
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
        matrix = multiplication(matrix,glavy,1/matrix[glavy][glavx],"gor")
        
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
matrix = sorting(matrix)
matrix = gotoint(matrix)

#=======================вывод матрицы
draw(matrix)  