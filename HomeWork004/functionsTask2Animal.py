from operator import attrgetter
from Animal import Animal
import os

def Task_Task2():
    print(
        '''
\tTask2. Создайте класс Animal со свойствами (созданными при помощи декораторов) для хранения:
\t•	клички животного, 
\t•	веса (в кг), 
\t•	возраста (в полных годах), 
\t•	цвета (масть) животного, 
\t•	фамилии и инициалов владельца (Иванов И.И., …).
\tРеализуйте конструктор __init__(), свойства, метод __str__(), метод вывода данных животного в виде строки таблицы. 
\tСоздайте при помощи конструкторов список из 10 животных, выведите список в консоль. 
\tРазработайте функцию, при помощи цикла находящую всех животных, возраст которых больше заданного с клавиатуры. Поместить найденных животных в дополнительный список, удалив животных из исходного списка. Выводите в консоль списки до и после вызова этой функции.
\tРеализуйте сортировки списка животных:
\t•	По убыванию возраста
\t•	По кличке
\t•	По возрасту и по цвету
'''
        )


list_items = []            # список

def Run_Task2():
    pass
    task1()
    task2(list_items)
    task3(list_items)
    task4(list_items)
    task5(list_items)
    

# возвращает список товаров для обработки
def animals_initializer():
    return [
        Animal('Котеечка', 5, 7, 'белоснежная', 'Иван','Ивушкин'),            # 1
        Animal('Темка', 2, 3, 'черный', 'Кирил','Михеев'),            # 2
        Animal('Пушистик', 6, 7, 'пегой', 'Антоха','Арузов'),            # 3
        Animal('Генерал', 4, 6, 'рыжая', 'Василина','Лоза'),            # 4
        Animal('Соня', 2, 7, 'серая', 'Елизавета','Домкратова'),            # 5
        Animal('Потапыч', 1, 3, 'белоснежная', 'Кирил','Васильевич'),            # 6
        Animal('Тимошка', 1, 2, 'белоснежная', 'Димон','Ивушкин'),            # 7
        Animal('Лизка', 2, 7, 'белоснежная', 'Василий','Ивушкин'),            # 8
        Animal('Певун', 4, 6, 'белоснежная', 'Иван','Ивушкин'),            # 9
        Animal('Обжора', 15, 1, 'белоснежная', 'Альфред','Ивушкин'),            # 10
    ]

_dir = 'Task4'
_file_name = 'animals.dat'
def generate_list(show=True):
    global list_items

    # если файл данных не найден - создать папку (если ее еще нет),
    # сгенерировать список, сохранить список в файле данных
    # иначе - загрузить список товаров из файла данных
    path_file = _dir + '/' + _file_name

    if not os.path.exists(path_file):
        list_items = animals_initializer()      # сгенерировать список товаров
        if not os.path.exists(_dir):           # создать папку для файла данных
            os.mkdir(_dir)
        # end if
        Animal.write_list(path_file, list_items)     # записать файл данных
    # end if
    list_items = Animal.read_list(path_file)     # чтение файла данных

    # выведем сформированный список товаров, если установлен параметра show
    if show:
        Animal.show_list('\n\tСформирован список', list_items)
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
        new_list_items = []            # список
        cnt = int(input('Введите возраст животных'))
        for item in list_items:
            if(item.age>=cnt):
                new_list_items.append(item)
        for item in new_list_items:
            list_items.remove(item)
        Animal.show_list('Collection животных с возрастом выше заданного',new_list_items)
        Animal.show_list('Collection исходная коллекция',list_items)

    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(list_items:list):
    try:
        pass        
        Animal.show_list('Collection Sort by Age Reverse',sorted(list_items,key=attrgetter('age'),reverse=True))

    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task4(list_items:list):
    try:
        pass
        Animal.show_list('Collection Sort by AnimalNames',sorted(list_items,key=attrgetter('animalNames'),reverse=True))
     
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task5(list_items:list):
    try:
        pass
        Animal.show_list('Collection Sort by Age and Colors',sorted(list_items,key=attrgetter('age','colors')))
       
    except Exception as ex:
        print("Общее исключение")
        print(ex)


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork004 import main
    main()
# end if