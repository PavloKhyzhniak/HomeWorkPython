# Модуль OS и работа с файловой системой
import os
from Figure2D import Figure2D
from Figure3D import Figure3D

from Triangle import Triangle
from Rectangle import Rectangle

from Cylinder import Cylinder
from Cone import Cone
from TrihedralPyramid import TrihedralPyramid


def Task_Task3():
    print(
        '''
\tTask 3. Создать иерархию классов:
\t•	Базовый класс Фигура2D со свойством для хранения длины одной стороны фигуры, с пустыми методами для вычисления площади и периметра (имеются в виду объявления вида def area(): pass и def volume(): pass)
\t•	Базовый класс Фигура3D со свойством радиус, пустыми методами для вычисления площади и объема
\t•	Класс Треугольник, наследует от Фигура2D, переопределяет методы для вычисления площади и периметра 
\t•	Класс Прямоугольник, наследует от Фигура2D, переопределяет методы для вычисления площади и периметра
\t•	Класс Цилиндр, наследует от Фигура3D с методами для вычисления площади и объема
\t•	Класс Конус, наследует от Фигура3D с методами для вычисления площади и объема
\t•	Класс ТрехграннаяПирамида, наследует от Фигура3D с методами для вычисления площади и объема (правильная трехгранная пирамида для упрощения вычислений)
\t•	реализовать по два объекта каждого типа в списке наследников класса Фигура2D, вычислить суммарную площадь фигур, суммарный периметр фигур
\t•	реализовать по два объекта каждого типа в списке наследников класса Фигура3D, вычислить суммарную площадь фигур, суммарный объем фигур 
'''
        )


list_items1 = []            # список
list_items2 = []            # список

def Run_Task3():
    pass
    task1()
    task2(list_items1)
    task2(list_items2)

# возвращает список товаров для обработки
def figure2d_initializer():
    return [
        Triangle( 5 ),            # 1
        Triangle( 2 ),            # 2
        Triangle( 6),            # 3
        Rectangle( 4),            # 4
        Rectangle( 2),            # 5
        Rectangle( 1),            # 6
    ]

def figure3d_initializer():
    return [
        Cylinder( 5, 7),            # 1
        Cylinder( 2, 3),            # 2
        Cylinder( 6, 7),            # 3
        Cone( 4, 6),            # 4
        Cone( 2, 7),            # 5
        Cone( 1, 3),            # 6
        TrihedralPyramid( 1, 2),            # 7
        TrihedralPyramid( 2, 7),            # 8
        TrihedralPyramid( 4, 6),            # 9
    ]

_dir = 'Task4'
_file_name1 = 'figure2d.dat'
_file_name2 = 'figure3d.dat'
def generate_list1(show=True):
    global list_items1

    # если файл данных не найден - создать папку (если ее еще нет),
    # сгенерировать список, сохранить список в файле данных
    # иначе - загрузить список товаров из файла данных
    path_file = _dir + '/' + _file_name1

    if not os.path.exists(path_file):
        list_items1 = figure2d_initializer()      # сгенерировать список товаров
        if not os.path.exists(_dir):           # создать папку для файла данных
            os.mkdir(_dir)
        # end if
        Figure2D.write_list(path_file, list_items1)     # записать файл данных
    # end if
    list_items1 = Figure2D.read_list(path_file)     # чтение файла данных

    # выведем сформированный список товаров, если установлен параметра show
    if show:
        Figure2D.show_list('\n\tСформирован список', list_items1)
    # end if
# end generate_list

def generate_list2(show=True):
    global list_items2

    # если файл данных не найден - создать папку (если ее еще нет),
    # сгенерировать список, сохранить список в файле данных
    # иначе - загрузить список товаров из файла данных
    path_file = _dir + '/' + _file_name2

    if not os.path.exists(path_file):
        list_items2 = figure3d_initializer()      # сгенерировать список товаров
        if not os.path.exists(_dir):           # создать папку для файла данных
            os.mkdir(_dir)
        # end if
        Figure3D.write_list(path_file, list_items2)     # записать файл данных
    # end if
    list_items2 = Figure3D.read_list(path_file)     # чтение файла данных

    # выведем сформированный список товаров, если установлен параметра show
    if show:
        Figure3D.show_list('\n\tСформирован список', list_items2)
    # end if
# end generate_list

def task1():
    try:
        pass    
        generate_list1(True)
        generate_list2(True)
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task2(list_items:list):
    try:
        pass
        sum1 = 0
        sum2 = 0
        for item in list_items:
            if isinstance(item, Figure3D):
                sum1+=item.area()
                sum2+=item.volume()
            elif isinstance(item, Figure2D):
                sum1+=item.area()
                sum2+=item.perimeter()
        if isinstance(list_items[0], Figure3D):
            print(f'Summary Area = {sum1:10}\nSummary Volume = {sum2:10}')
            Figure3D.show_list('Collection ',list_items)
        elif isinstance(list_items[0], Figure2D):
            print(f'Summary Area = {sum1:10}\nSummary Perimeter = {sum2:10}')
            Figure2D.show_list('Collection ',list_items)
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(list_items:list):
    try:
        pass
        
    except Exception:
        print("Общее исключение")
        print()

def task4(list_items:list):
    try:
        pass
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork004 import main
    main()
# end if