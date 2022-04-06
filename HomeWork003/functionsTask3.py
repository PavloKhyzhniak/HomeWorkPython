# Модуль OS и работа с файловой системой
import os
import shelve
import sys


def Task_Task3():
    print(
        '''
        •	Task3. При помощи модуля os создайте в проекте папку task3, выведите в бинарный файл при помощи модуля shelve список товаров. Каждый элемент списка также список – наименование, цена, признак наличия. В качестве ключа используйте порядковый номер товара в списке.  Если файла в папке task3 нет – формируйте список для записи присваиванием и сохраняйте его в файл. Список товаров должен содержать от 10 до 15 товаров. Загрузить список из бинарного файла shelve, вычислить сумму цен товаров, имеющихся в наличии и количество наименований товаров, которых нет в наличии. Реализуйте добавление, изменение и удаление товара из файла по командам меню задачи.  
'''
        )

def Run_Task3():
    pass
    task1('task3')
    task2('product.bin')
    task3('product.bin')
    task4()

product = [
        ["конфеты Тимофей", 229,False],
        ["шоколад Алиса", 343,True],
        ["рисовые шарики", 337,False],
        ["почечные колики", 553,False],
        ["инсульт в 30", 34,False],
        ["сила Богов с утра", 63,True],
        ["вечерний закат", 331,True],
        ["обеденный провал", 323,False],
        ["кожа девственника", 133,False],
        ["вырви глаз", 233,True],
        ["смешарики из преисподни", 33,True],
        ["печенье Борис", 27,True]
    ]


def task1(dirname):
    try:
        pass
        if(os.path.isdir(sys.path[0] + "\\" + dirname)):
            os.rmdir(sys.path[0] + "\\" + dirname)
        # путь относительно текущего скрипта
        os.mkdir(sys.path[0] + "\\" + dirname)

    except Exception:
        print("Общее исключение")

def task2(filename):
    try:
        pass
        i=0
         # запись файла при помощи модуля shelve
        with shelve.open(sys.path[0] + "\\" + filename) as file:
            for state in product:
                i+=1
                # 'states[state] =' вместе с присваиванием это и есть запись в файл
                file[f'{i}'] = state#f'{state[0]}:{state[1]}:{state[2]}'
            # end for
        # end with
        print(f'\tФайл \033[34;1m{filename}\033[0m данных записан')
        print()

    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(filename):
    try:
        pass
        print("Считаем из файла")
        with shelve.open(sys.path[0] + "\\" + filename) as file:
            product = list()
            for product_item in file:
                print(f'{file[product_item]}')
                product.append(file[product_item])
            # end for
        # end with
        print()

    except Exception:
        print("Общее исключение")
        print()

def task4():
    try:
        pass
        sum=0
        cnt=0
        print("Подведем итоги")
        for item in product:
            print(f'{item}')
            if(item[2]):
                sum+=item[1]
            else:
                cnt+=1
        print(f'Summa available product : = {sum}')
        print(f'Count not available product : = {cnt}')
        print()

    except Exception:
        print("Общее исключение")


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork003 import main
    main()
# end if