import os
from TVShop import TVShop
from GUI.mainGUI import GUI_HW005_task01

def Task_Task1():
    print(
        '''
\tTask1. Разработайте приложение Python с использованием Tkinter. для ввода данных об объекте класса Телевизор. Храните данные в бинарном файле с использованием модуля shelve.
\tДанные из таблицы выводите в метку Label с моноширинным шрифтом. Для добавления данных в таблицу используйте кнопку Button, команду меню.
\tКласс Телевизор с полями для хранения 
\t•	производителя и типа телевизора, это одно поле (используйте Combobox для выбора конкретного значения), 
\t•	диагональ экрана, 
\t•	разрешения по вертикали, 
\t•	разрешения по горизонтали,
\t•	наличие разъема CF
\t•	наличие разъема HDMI
\t•	наличие разъема USB 
\t•	цена.
\t Реализуйте обработки:
\t•	сортировка по убыванию цены
\t•	сортировка по производителю и типу
'''
        )

list_items = []            # список

def Run_Task1():
    pass
    task1()
    GUI_HW005_task01.Show(list_items)
    

# возвращает список товаров для обработки
def tvshops_initializer():
    return TVShop.initialized()

_dir = 'Task5'
_file_name = 'tvshop.dat'
def generate_list(show=True):
    global list_items

    # если файл данных не найден - создать папку (если ее еще нет),
    # сгенерировать список, сохранить список в файле данных
    # иначе - загрузить список товаров из файла данных
    path_file = _dir + '/' + _file_name

    if not os.path.exists(path_file):
        list_items = tvshops_initializer()      # сгенерировать список товаров
        if not os.path.exists(_dir):           # создать папку для файла данных
            os.mkdir(_dir)
        # end if
        TVShop.write_list(path_file, list_items)     # записать файл данных
    # end if
    list_items = TVShop.read_list(path_file)     # чтение файла данных

    # выведем сформированный список товаров, если установлен параметра show
    if show:
        TVShop.show_list('\n\tСформирован список', list_items)
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
        TVShop.show_list('Collection',list_items)
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(list_items:list):
    try:
        pass
        
    except Exception as ex:
        print("Общее исключение")
        print(ex)



# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork005 import main
    main()
# end if