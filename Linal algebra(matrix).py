from fractions import Fraction
import copy
class Matrix:
    oprkoef = 1
    rang = 1
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
    #полезные функции 
    def sorting(self):#сортировка матрицы по количеству главенствующих нулей(ступенчатый вид)
        #подумать как узнать знак определителя отсортированной матрицы
        k = len(self.matrix)
        for i in range(len(self.matrix)):
            countr = 0
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    countr+=1
                else:
                    self.matrix[i].append(countr)
                    break
            if len(self.matrix[i]) == k:
                self.matrix[i].append(0)
        self.matrix.sort(key = lambda x: x[-1])
        
        for i in range(len(self.matrix)):
            del self.matrix[i][-1]
    def draw(self):#выводит матрицу на экран

        print("==================")
        for i in range(len(self.matrix)):
            print(*self.matrix[i])
        print("==================")       
    def gotoFraction(self):#перевод в простые дроби
        for i in range(len(self.matrix)):
                self.matrix[i] = list(map(Fraction,self.matrix[i]))           
    def gotoint(self):#если возможно перейти к целым числам 
        flag = 1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != int(self.matrix[i][j]):
                    flag = 0
        if flag:
            for i in range(len(self.matrix)):
                self.matrix[i] = map(int,self.matrix[i])
    @staticmethod
    def Matrix_copy(matrix):#метод копирования матрицы
        return copy.deepcopy(matrix)

    #переменная axis принимает значения "gor" и "vert"
    #три элементарных преобразования
    def perestan(self,x,y,axis):#перестановка строк или столбцов 
        self.oprkoef *= -1
        if axis == "gor":
            self.matrix[x],self.matrix[y] = self.matrix[y],self.matrix[x]
        else:
            for ind in range(len(self.matrix)):
                self.matrix[ind][x],self.matrix[ind][y] = self.matrix[ind][y],self.matrix[ind][x]
    def multiplication(self,ind,koef,axis):# умножение строки или столбца на число
        self.oprkoef *= koef
        if axis == "gor":
            for i in range(len(self.matrix[ind])):
                self.matrix[ind][i] *= koef
        else:
            for i in range(len(self.matrix)):
                self.matrix[i][ind] *= koef
    def increase(self,x,y,koef,axis):#прибавление к одной строке другую помноженную на коэффициент у
        #x - главная строка, у - которую прибавляют
        if axis == "gor":
            for i in range(len(self.matrix[x])):
                self.matrix[x][i] += koef * self.matrix[y][i]
        else:
            for i in range(len(self.matrix)):
                self.matrix[i][x] += koef * self.matrix[i][y]
   
    #функции расчёта определителей
    def opred2(self): #матрица только 2 на 2! полностью переписать
        if len(self.rows) != 2 or len(self.columns) != 2:
            return -1        
        else:
            return (self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0])
    def opred3(self): #матрица только 3 на 3 ! аналогично 
        if len(self.rows) != 3 or len(self.columns) != 3:
            return -1
        else: 
            return ((self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]) +
                    (self.matrix[1][0] * self.matrix[2][1] + self.matrix[0][2]) +
                    (self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]) -
                    (self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]) -
                    (self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]) -
                    (self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]) 
                    )
    def opredn(self): #матрица n-го порядка (не реализована) 
        if self.rows != self.columns:
            print("матрица не квадратная(функция opredn)")
            return -1
        if self.rows == 1:
            return self.matrix[0]
        if self.rows == 2:
            self.opred2()
        if self.rows == 3:
            self.opred3()
        else:#придумать как сделать рекурсию с подматрицами
            pass

    def transpon(self):#транспонирование матрицы
        for i in range(len(self.matrix)):
            for j in range(i,len(self.matrix[0])):
                self.matrix[i][j],self.matrix[j][i] = self.matrix[j][i],self.matrix[i][j]
    def obratmat(self):#обратная матрица(только для квадратных матриц)
        if self.columns != self.rows:
            print("матрица не квадратная функция(obrat)")
            return -1
        #создание матрицы Г(а)
        algdop = [[0 for i in range(self.columns*2)] for j in range(self.rows)]
        for i in range(self.columns):
            for j in range(self.rows):
                algdop[i][j] = self.matrix[i][j]
        for i in range(self.rows):
            algdop[i][i+self.columns] = 1
        algdop = Matrix(algdop)
        algdop.gotoFraction()

        for glav in range(algdop.rows):
             # индексы главного элемента - [i][i] 
            for j in range(algdop.rows):
                if j == glav :
                    pass 
                else:
                    if algdop.matrix[glav][glav] == 0:
                        algdop.increase(glav,glav+self.columns,1,"vert")
                    algdop.increase(j,glav,(-1)*(algdop.matrix[j][glav]/algdop.matrix[glav][glav]),"gor")            
            algdop.multiplication(glav,1/algdop.matrix[glav][glav],"gor")

        #выведение массива
        print("==================")
        for i in range(algdop.rows):
            self.matrix[i] = algdop.matrix[i][self.columns:]
            
    def Stupmatrix(self): #работает корректно, но можно сделать лучше
        glavx = 0 # место главы строки(столбец)
        glavy = 0 # главная строка, по которой проходит обнуление ряда(строка)
        for glavy in range(len(self.matrix)-1):
            #1)найти индекс главы строки
            for i in range(len(self.matrix[glavy])):
                if (self.matrix[glavy][i] != 0) and (self.matrix[glavy][i] != Fraction(0,1)):
                    glavx = i
                    break
            if self.matrix[glavy][glavx] == 0:
                self.matrix[glavy][glavx] = 1
            #2)умножить строку на 1/глава, чтобы глава стал равен 1
            self.multiplication(glavy,1/self.matrix[glavy][glavx],"gor")

            #3)обнулить столбец главы(кроме него), прибавив к каждой строке ниже главы строку главы умноженную на -1* элемент стоящий под главой
            for i in range(glavy+1,len(self.matrix)):
                self.increase(i,glavy,-1*self.matrix[i][glavx],"gor")    
        self.sorting()

        glavx = 0 # место главы строки(столбец)
        glavy = 0 # главная строка, по которой проходит обнуление ряда(строка)
        for glavy in range(len(self.matrix)-1):
            #1)найти индекс главы строки
            for i in range(len(self.matrix[glavy])):
                if (self.matrix[glavy][i] != 0) and (self.matrix[glavy][i] != Fraction(0,1)):
                    glavx = i
                    break
            if self.matrix[glavy][glavx] == 0:
                self.matrix[glavy][glavx] = 1
            #2)умножить строку на 1/глава, чтобы глава стал равен 1
            self.multiplication(glavy,1/self.matrix[glavy][glavx],"gor")

            #3)обнулить столбец главы(кроме него), прибавив к каждой строке ниже главы строку главы умноженную на -1* элемент стоящий под главой
            for i in range(glavy+1,len(self.matrix)):
                self.increase(i,glavy,-1*self.matrix[i][glavx],"gor") 
        
    def rang(self):    #определяет ранг матрицы(не работает)
        #сведение к поиску диагонали ненулевых элементов максимальной длины
        rang = 0
        self.Stupmatrix()
        for i in range(len(self.matrix)):
            if self.matrix[i][i] != 0:
                rang+=1

    @staticmethod
    def matrix_sum(matrix1,matrix2):    #работает корректно с матрицами одинакового размера
        multimatrix = [[0 for el in range(len(matrix1[0]))] for el in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                multimatrix[i][j] = matrix1[i][j] + matrix2[i][j]

        return multimatrix
    @staticmethod
    def matrix_multiplication(matrix1,matrix2):   #работает корректно при кол-во столбцов 1 матрицы = кол-во строк 2 матрицы
        #Работает корректно
        #а - строки, b - столбцы, перемножать матрицы можно только если a2 = b1
        multimatrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                summ = 0
                for k in range(len(matrix1[i])):
                    summ+=matrix1[i][k] * matrix2[k][j]
                multimatrix[i][j] = summ
        return multimatrix

#сделать переход к матрице улучшенного вида
#=======================ввод
L = int(input())
matrix = []
for i in range(L):
    matrix.append(list(map(Fraction,input().split())))
#=======================основное тело
matrix = Matrix(matrix)
#=======================вывод матрицы
matrix2.draw()
