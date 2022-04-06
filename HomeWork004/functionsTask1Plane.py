from Plane import Plane
import os

def Task_Task1():
    print(
        '''
\tTask1. Разработайте класс Plane со следующими свойствами (созданными при помощи декораторов):
\t•	тип самолета (Ил-76, Boeing-747, …)
\t•	количество пассажирских мест (целое число, от 0 и выше)
\t•	текущее количество пассажиров
\t•	расход горючего за час полета (вещественное число, от 0 и выше)
\t•	количество двигателей (целое число, от 1 до 12)
\t•	название авиакомпании – владельца (непустая строка)
\tВ свойствах-сеттерах выбрасывайте исключение при некорректных значениях. Разработайте конструктор __init__() и метод формирования строкового представления __str__() в виде строки таблицы.
\tСоздайте список самолетов (не менее 10 элементов). Разработайте функции для обработки списка:
\t•	Вывод списка самолетов в виде таблицы
\t•	Увеличение количества пассажиров на введенное с клавиатуры значение
\t•	Удаление выбранного по номеру в списке самолета 
'''
        )

list_items = []            # список

def Run_Task1():
    pass
    task1()
    task2(list_items)
    task3(list_items)


# возвращает список товаров для обработки
def planes_initializer():
    return [
        Plane('Ил-76', 20, 10, 300, 2,'РоссКосмос'),            # 1
        Plane('Ил-76', 20, 11, 300.3, 2,'РоссКосмос'),            # 2
        Plane('Ил-76', 20, 12, 300.3, 2,'РоссКосмос'),            # 3
        Plane('Ил-76', 20, 13, 300.3, 2,'РоссКосмос'),            # 4
        Plane('Ил-76', 20, 14, 300.3, 2,'РоссКосмос'),            # 5
        Plane('Ил-76', 20, 15, 300.3, 2,'РоссКосмос'),            # 6
        Plane('Ил-76', 20, 16, 300.3, 2,'РоссКосмос'),            # 7
        Plane('Ил-76', 20, 17, 300.3, 2,'РоссКосмос'),            # 8
        Plane('Ил-76', 20, 18, 300.3, 2,'РоссКосмос'),            # 9
        Plane('Ил-76', 20, 19, 300.3, 2,'РоссКосмос'),            # 10
        Plane('Ил-76', 20, 20, 300.3, 2,'РоссКосмос'),            # 11
        Plane('Ил-76', 20,  1, 300.3, 2,'РоссКосмос')             # 12
    ]

_dir = 'Task4'
_file_name = 'planes.dat'
def generate_list(show=True):
    global list_items

    # если файл данных не найден - создать папку (если ее еще нет),
    # сгенерировать список, сохранить список в файле данных
    # иначе - загрузить список товаров из файла данных
    path_file = _dir + '/' + _file_name

    if not os.path.exists(path_file):
        list_items = planes_initializer()      # сгенерировать список товаров
        if not os.path.exists(_dir):           # создать папку для файла данных
            os.mkdir(_dir)
        # end if
        Plane.write_list(path_file, list_items)     # записать файл данных
    # end if
    list_items = Plane.read_list(path_file)     # чтение файла данных

    # выведем сформированный список товаров, если установлен параметра show
    if show:
        Plane.show_list('\n\tСформирован список', list_items)
    # end if
# end generate_list

def task1():
    try:
        pass
        generate_list(True)
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task2(list_items:list):
    try:
        pass
        cnt = int(input('На сколько увеличить пассажиров на рейсах'))
        for item in list_items:
            item.countPassenger =item.countPassenger+cnt
        Plane.show_list('Collection',list_items)
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(list_items:list):
    try:
        pass
        cnt = len(list_items)
        while(cnt>=len(list_items)):
            cnt = int(input('Удаление выбранного по номеру в списке самолета'))
        list_items.pop(cnt)            
        print('Удаление произведено')
        Plane.show_list('Collection',list_items)
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork004 import main
    main()
# end if