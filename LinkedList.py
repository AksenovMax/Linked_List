import pygame as pg
import sys


class LinkedList:
    def __init__(self):
        self.mainlist = []

    # добавляем элемент Н в конец
    def add_end(self, n):
        return self.mainlist.append(n)

    # Вставляем на место Н объект Х
    def innsert(self, n, x):
        # Если список пустой, и вставляем на 1 позицию
        if len(self.mainlist) == 0 and n == 0:
            return self.mainlist.insert(n, x)
        # Запрещаем вставлять, если индекс слишком большой
        elif n >= len(self.mainlist):
            print('неверное значение')
        else:
            return self.mainlist.insert(n, x)

    # Выводим весь список
    def show(self):
        return self.mainlist

    # Удаляем 1 элемент
    def del_1st(self):
        if len(self.mainlist) > 0:
            return self.mainlist.pop(0)
        else:
            print('неверное значение')


    # Удаляем последний элемент
    def del_last(self):
        if len(self.mainlist) > 0:
            return self.mainlist.pop()
        else:
            print('неверное значение')

    # Удаляем Н элемент из списка
    def del_n(self, n):
        if n >= len(self.mainlist):
            print('нет такого элемента')
        else:
            return self.mainlist.pop(n)

    # Узнаем элемент по индексу
    def element_n(self, n):
        if n >= len(self.mainlist):
            print('нет такого элемента')
        else:
            return self.mainlist[n]

    # Узнаем длину списка
    def Len(self):
        lenn = len(self.mainlist)
        return lenn

    # Создаем итератор
    def __iter__(self):
        return iter(self.mainlist)

    # Получаем строку по списку
    def str(self):
        stroka = ""
        for elem in self.mainlist:
            stroka += str(elem) + " "
        return stroka

    # Быстрая сортировка
    def quick(self, A):
        if len(A) <= 1:
            return A
        middle = A[len(A) // 2]
        more_list, same_list, less_list = [], [], []
        for elem in A:
            if elem < middle:
                more_list.append(elem)
            elif elem == middle:
                same_list.append(elem)
            else:
                less_list.append(elem)
        return self.quick(less_list) + same_list + self.quick(more_list)


class Point2d:
    def __init__(self, x):
        self.x = x

    # Сложение
    def __add__(self, z):
        return self.x + z

    # Вычитание
    def __sub__(self, z):
        return self.x - z

    # Умножение
    def __mul__(self, z):
        return self.x * z

# Создаем экземпляр класса LinkedList
obj = LinkedList()

# Управление с клавиатуры
while True:
    print('1 - Работа со списком в LinkedList')
    print('2 - Работа с программой PyGame')
    choice = int(input('Сделайте выбор '))
    if choice == 1:
        while True:
            print('1 - Добавить в конец')
            print('2 - Добавить по индексу')
            print('3 - Удалить первый элемент')
            print('4 - Удалить последний элемент')
            print('5 - Удалить элемент по индексу')
            print('6 - Вывести весь список')
            print('7 - Выход')
            print('8 - Быстрая сортировка (от большего к меньшему)')

            choice_LinkedList = int(input('Сделайте выбор '))

            if choice_LinkedList == 1:
                obj.add_end(int(input('Введите число ')))

            if choice_LinkedList == 2:
                obj.innsert(int(input('Введите позицию ')), int(input('Введите число  ')))

            if choice_LinkedList == 3:
                obj.del_1st()

            if choice_LinkedList == 4:
                obj.del_last()

            if choice_LinkedList == 5:
                obj.del_n(int(input('Введите позицию  ')))

            if choice_LinkedList == 6:
                print(obj.show())

            if choice_LinkedList == 7:
                print ('-----------------------')
                print(f'Список - {obj.show()}')
                print(f'Длина списка - {obj.Len()}')
                print(f'Список строкой - {obj.str()}')
                print('Iter')
                for elem in obj.show():
                    print(elem)
                break

            if choice_LinkedList == 8:
                a = obj.mainlist
                b = obj.quick(a)
                print(obj.quick(a))
                obj.mainlist = b

    if choice == 2:
        click = 0
        # Создаем экземпляр класса LinkedList
        points = LinkedList()
        # Названия цветов
        green = (0, 225, 0)
        another_blue = (128, 128, 255)
        blue = (0, 0, 225)
        orange = (255, 100, 10)
        brown = (100, 40, 0)
        highlighter = (255, 255, 100)
        red = (255, 0, 0)
        # Ширина линии
        widht = 4
        # Настройка экрана PyGame
        screen = pg.display.set_mode((900, 600))
        screen.fill(another_blue)
        pg.display.update()
        clock = pg.time.Clock()
        pg.display.set_caption("Игра")

        # Действия на экране программы
        work = True
        while work:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                # Нажатие на мышь
                if i.type == pg.MOUSEBUTTONDOWN:
                    # Нажатие на ЛКМ ( = кнопка 1)
                    if i.button == 1:
                        # Добавляем в конец нашего списка сначала Х, а затем У. Теперь Х минус второй элемент (-2), а У - минус 1(-1)
                        points.add_end(i.pos[0])
                        points.add_end(i.pos[1])
                        # Рисуем точку коричневую в месте клика
                        pg.draw.circle(screen, brown, i.pos, 20)
                        # Если клик уже не первый (изначально он 0, при нажатии +=1), рисуем линию с координатами, равными значениям списка
                        if click >= 1:
                            pg.draw.line(screen, green, [points.element_n(-4), points.element_n(-3) ], [points.element_n(-2), points.element_n(-1)], widht)
                        click += 1
                        pg.display.update()
                    # Нажатие на ПКМ ( = кнопка 3)
                    elif i.button == 3:
                        d1 = Point2d(i.pos[0])   # Создаем экземпляр класса с математическими операциями ДЛЯ Х
                        d2 = Point2d(i.pos[1])   # Создаем экземпляр класса с математическими операциями ДЛЯ У
                        # Рисуем 4 линии, используя класс с операциями, который мы сделали (как в задании)
                        pg.draw.line(screen, blue, [i.pos[0], i.pos[1]], [d1.__add__(50), i.pos[1]], widht)
                        pg.draw.line(screen, red, [i.pos[0], i.pos[1]], [i.pos[0], d2.__add__(50)], widht)
                        pg.draw.line(screen, orange, [d1.__add__(50), i.pos[1]], [d1.__add__(50), d2.__add__(50)], widht)
                        pg.draw.line(screen, highlighter, [i.pos[0], d2.__add__(50)], [d1.__add__(50), d2.__add__(50)], widht)
                        pg.display.update()
                    # Нажатие на колесико мыши ( = кнопка 2)
                    elif i.button == 2:
                        # очищаем экран и делаем число кликов == 0, чтобы линия рисовалась только при 2 и более клике
                        screen.fill(another_blue)
                        pg.display.update()
                        click = 0

                # Нажатие на клавишу q
                if i.type == pg.KEYDOWN:
                    if i.key == pg.K_q:
                        work = False
            pg.time.delay(20)









