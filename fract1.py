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
    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value
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

        for part in self.state:
            if part == "F":
                self.t.forward(self.length)
            elif part == "+":
                self.t.left(self.angle)
            elif part == "-":
                self.t.right(self.angle)
        
        turtle.done()

class Shape:
    #возле каждого фрактала помечено рекомендуемое число итераций
    @staticmethod
    def Koh_line(iterations,speed = 1,f_len = 10,pen_width = 2):    # 2-8 итераций
        angle = 60
        turtle.tracer(speed,0)
        l_sys = SystemL(t,"F",pen_width,f_len,angle)
        l_sys.add_rules(("F", "F+F--F+F"))
        l_sys.generate_path(iterations)
        l_sys.draw_turtle((-60-100*iterations,0-25*iterations), 0)
    @staticmethod
    def Koh_star(iterations,speed = 1,f_len = 10,pen_width = 2):    # 4-7 итераций
        angle = 60
        turtle.tracer(speed,0)
        l_sys = SystemL(t,"F--F--F",pen_width,f_len,angle)
        l_sys.add_rules(("F", "F+F--F+F"))
        l_sys.generate_path(iterations)
        l_sys.draw_turtle((0-50*iterations,0+25*iterations), 0)
    @staticmethod
    def Koh_square(iterations,speed = 1,f_len = 10,pen_width = 2):  # 1-4 итераций
        angle = 90
        turtle.tracer(speed,0)
        l_sys = SystemL(t,"F+F+F",pen_width,f_len,angle)
        l_sys.add_rules(("F", "F-F+F+FFF-F-F+F"))
        l_sys.generate_path(iterations)
        l_sys.draw_turtle((0-50*iterations,0-50*iterations), 0)
    @staticmethod
    def crystal(iterations,speed = 1,f_len = 10,pen_width = 2):     # 3-6 итераций
        angle = 90
        turtle.tracer(speed,0)
        l_sys = SystemL(t,"F+F+F+F",pen_width,f_len,angle)
        l_sys.add_rules(("F", "FF+F++F+F"))
        l_sys.generate_path(iterations)
        l_sys.draw_turtle((0-50*iterations,0-50*iterations), 0)
    @staticmethod
    def seg_curve32(iterations,speed = 1,f_len = 10,pen_width = 2): # 1-3 итераций
        angle = 90
        turtle.tracer(speed,0)
        l_sys = SystemL(t,"F+F+F+F",pen_width,f_len,angle)
        l_sys.add_rules(("F", "-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"))
        l_sys.generate_path(iterations)
        l_sys.draw_turtle((0-100*iterations,0-100*iterations), 0)


#базовые параметры
width = 1920
height = 1080
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
t =turtle.Turtle()
t.ht()
#=================
#time.sleep(10)
Shape.crystal(6,9,1)