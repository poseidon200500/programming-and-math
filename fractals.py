import turtle 
import time

class SystemL:

    def __init__(self,t,axiom,width,length,angle):
        self.axiom = axiom          # инициатор
        self.state = axiom          # строка с набором команд (F,+,-)
        self.width = width          # толщина линии рисования
        self.length = length        # длина одного линейного сигмента
        self.angle = angle          # фиксированный угол поворота
        self.t = t                  # черепашка
        self.rules = {}             #словарь правил
        self.t.pensize(self.width)  # установка толщины пера
    
    def add_rules(self, rules): #на вход подавать кортеж содержащий кортежи-правила
        for rule in rules:
            self.rules[rule[0]] = rule[1]

    def generate_path(self,iter):
        for n in range(iter):
            #self.length = self.length / iter
            for key,value in self.rules.items():
                #заменяем F на правило, при этом понижаем регистр, чтобы при большом количестве правил они не наслаивались
                self.state = self.state.replace(key,value.lower()) 

            self.state = self.state.upper()                   
    def draw_turtle(self,start_pos,start_angle):
        #устанавливаем скоростной режим черепашки
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()
        miny = start_pos[1]
        maxy = start_pos[1]
        for part in self.state:
            if part == 'F':
                self.t.forward(self.length)


            elif part == '+':
                self.t.left(self.angle)
            elif part == '-':
                self.t.right(self.angle)
        
        

class Shape:
    @staticmethod
    def Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos):
        turtle.tracer(speed,0)
        l_sys = SystemL(t,axiom,pen_width,f_len,angle)
        l_sys.add_rules(rules)
        l_sys.generate_path(iterations)
        l_sys.draw_turtle(start_pos, 0)
    #возле каждого фрактала помечено рекомендуемое число итераций
    @staticmethod
    def Koh_line(iterations,speed = 1,f_len = 10,pen_width = 2):    # 2-8 итераций
        #расстояние по иксу равно 3**iter * f_len
        angle = 60
        axiom = 'F'
        rules = (('F', 'F+F--F+F'),)
        x_ots = 3**iterations * f_len/2
        start_pos = (0-x_ots/2,0-x_ots/2)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def Koh_star(iterations,speed = 1,f_len = 10,pen_width = 2):    # 4-7 итераций
        angle = 60
        axiom = 'F--F--F'
        rules = (('F','F+F--F+F'),)
        start_pos = (0-50*iterations,0+25*iterations)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def Koh_square(iterations,speed = 1,f_len = 10,pen_width = 2):  # 1-4 итераций
        angle = 90
        axiom = 'F+F+F'
        rules = (('F', 'F-F+F+FFF-F-F+F'),)
        start_pos = (0,0-50*iterations)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def crystal(iterations,speed = 1,f_len = 10,pen_width = 2):     # 3-6 итераций
        angle = 90
        axiom = 'F+F+F+F'
        rules = (('F', 'FF+F++F+F'),)
        start_pos = (0-50*iterations,0-50*iterations)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def seg_curve32(iterations,speed = 1,f_len = 10,pen_width = 2): # 1-3 итераций
        angle = 90
        axiom = 'F+F+F+F'
        rules = (('F', '-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+'),)
        start_pos = (0-100*iterations,0-100*iterations)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def Dragon_Harter(iterations, speed = 1,f_len = 10,pen_width = 2):#4-13 итераций
        angle = 90
        axiom = 'FX'
        rules = (('FX', 'FX+FY+'),('FY','-FX-FY'))
        start_pos = (0,0)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def Serpin_triangle(iterations, speed = 1,f_len = 10, pen_width = 2):
        angle = 60
        axiom = 'FXF--FF--FF--FF'
        rules = (('F','FF'),('X','--FXF++FXF++FXF--'))
        start_pos = (-200,-50)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)



    #======================================
    #======================================
    #авторские фракталы(сам реализовывал)
    @staticmethod #треугольник обратный серпинскому
    def Not_Serpin_triangle(iterations, speed = 1,f_len = 10, pen_width = 2):
        angle = 60
        axiom = 'FXF--FXF--FXF--FF'
        rules = (('F','FF'),('X','++FXF--FXF--FXF++'))
        start_pos = (-200,-50)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)

    def Plazma(iterations, speed = 1): # в процессе
        #base
        t.penup()
        t.goto()
#базовые параметры
width = 1920
height = 1080
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
t =turtle.Turtle()
t.ht()
#================= основное тело

Shape.Koh_line(5,3,5)

#================= не закрывает окно 
turtle.done()




