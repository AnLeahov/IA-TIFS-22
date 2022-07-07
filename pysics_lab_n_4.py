import time, math

#Переменные глобальной видимости
G = 9.8
dG = 0.01
Pi = 3.14
dPi = 0.01
dX = 0.001
dT = 0.05
#Список для хранения констант
CONST = [G, dG, Pi, dPi, dX, dT]

#списки для сохранения значений введных пользователем:
mass = [] #масс разновесов
x = [] #удлинения пружины
N = [] #кол-ва полных колебаний
t = [] #пройденного времени за N колебаний

#списки для сохранения значений вычисляемых значений:
To = [] #некая величина
dTo = [] #приставка d будет в дальнейшем означать "дельта"
T = [] #некая величина
dT = [] #некая величина

USER_DICTIONARES = [mass, x, N, t]   #ЗАМЕТКА: изначально предпологалось, что будут использоваться словари,
VALUE_DICTIONARES = [To, dTo, T, dT] #но от этой идеи пришлось отказаться. Сохраняются только
                                     #названия переменных, ничего общего со словорями не имеющими

EXCEL = {
1:'''+===+=====+=====+=====+=======+=====+====+=====+=====+''',
2:'''| № |  m  |  x  |  To |  ΔTo  |  N  | t  |  T  | ΔT  |''',
3:'''| %s |%s|%s|%s|%s| %s| %s|%s|%s|'''}


def display_info(): #Функция отображает необходимую информацию для пользователя
    print('''
С начала работы программы, полезные подсказки отображаться не будут.
Как только будет запущена стадия получения значений,
вы должны будете запомнить следующий порядок для их ввода:

1) масса - m (кг)
2) удлинение пружины - x (м)
3) кол-во необходимых полных колебаний - N 
4) время за которое происходит N полных колебаний - t (с)

ВАЖНО! Вводите сразу в преобразованные величины, как это требует программа.

ВАЖНО! В случае, если вы перепутали порядок ввода значений,
завершите программу и запустите ее снова.
Данное неудобство сохраняется для читабельности кода.

Приятного пользования!
''')
    time.sleep(3)

    
    

def get_values(): #Функция получает все необходимые значения для работы от пользователя
    #Обозначение переменных
    global USER_DICTIONARES
    #Под-функции
    def ccv():
        #create and check values
        #Создает значение, проверяет его возможность преобразования в float и возвращает его
        while True:
            try:
                value = float(input())
            except ValueError:
                print('Введите числовое значение.')
                continue
            else:
                return value

    #Введение значений пользователем
    for line in range(3): #Цифра 3 в range() равна кол-ву строк в таблице
        print('Вводите значения для строки №%s:' % (line+1))
        for dictionare in USER_DICTIONARES:
            value = ccv()
            dictionare.append(value)

def calculate_values(): #в функции вычисляются другие значения для заполнения таблицы
    #Обозначение переменных
    global USER_DICTIONARES, VALUE_DICTIONARES, CONST

    #вычисление
    for i in range(3):
        #вычисление To                       пи                    х                      g
        VALUE_DICTIONARES[0].append(float(2*CONST[2]*math.sqrt(USER_DICTIONARES[1][i]/CONST[0])))
        #вычисление dTo                    дельта пи   пи             дельта g   g               дельта x       x                     To
        VALUE_DICTIONARES[1].append(float(((CONST[3]/CONST[2])+(1/2)*(CONST[1]/CONST[0])+(1/2)*(CONST[4]/USER_DICTIONARES[1][i]))*VALUE_DICTIONARES[0][i]))
        #вычисление T                           t                      N
        VALUE_DICTIONARES[2].append(float(USER_DICTIONARES[2][i]/USER_DICTIONARES[3][i]))
        #вычисление dT                      дельта t        t                    T
        VALUE_DICTIONARES[3].append(float((CONST[5]/USER_DICTIONARES[2][i])*VALUE_DICTIONARES[2][i]))
        
def draw_board():
    #Обозначение переменных
    global USER_DICTIONARES, VALUE_DICTIONARES, EXCEL
    #Под-функции
    def h(numObj, digits=3): #определяет кол-во знаков после запятой и преобразует число в строку
        return f"{numObj:.{digits}f}"

    #Рисование таблицы
    print(EXCEL[1])
    print(EXCEL[2])
    for i in range(3):
        print(EXCEL[3] % ((i+1), h(USER_DICTIONARES[0][i]), h(USER_DICTIONARES[1][i]), h(VALUE_DICTIONARES[0][i]), h(VALUE_DICTIONARES[0][i], 5), USER_DICTIONARES[2][i], USER_DICTIONARES[3][i], h(VALUE_DICTIONARES[2][i]), h(VALUE_DICTIONARES[3][i])))
    print(EXCEL[1])
    
    
display_info()    
get_values()
calculate_values()
draw_board()
    
