import functionsTask3dictionary as func
import sys
import csv

def Task_Task2():
    print(
        '''
        •	Task2. Разработайте словарь с названиями ряда государств и их столицами. Реализуйте операции:
\to	вывод столицы заданного государства;
\to	вывод государства, столицей которого является заданный город;
\to	запись словаря в файл формата CSV, имя файл – countries.csv, имя жестко задано, реализовывать выбор из файловой системы не надо
\to	чтение словаря из файла формата CSV, имя файла – countries.csv, имя жестко задано, реализовывать выбор из файловой системы не надо
\to	добавление государства и его столицы в словарь
\tЕсли заданного государства или города в словаре нет, на экран должно выводиться соответствующее сообщение.
'''
        )

def Run_Task2():
    pass
    task1()
    task2()
    task3('countries.csv')
    task4('countries.csv')
    task5()

def task1():
    try:
        pass
        func.getCountries()
        country = input("Введите страну из приведенных выше: ")
        func.getCountryTown(country)
        print()
        input(f"Press Any Key....")
        print()
      
    except Exception:
        print("Общее исключение")

def task2():
    try:
        pass
        func.getCountryTowns()
        countrytown = input("Введите город из приведенных выше: ")
        func.getCountry(countrytown)
        print()
        input(f"Press Any Key....")
        print()
 
    except Exception as ex:
        print("Общее исключение")
        print(ex)

def task3(file_name):
    try:
        pass
        print(f'Write to File dictionary')
        with open(sys.path[0] + "\\" + file_name, "w", encoding='UTF-8', newline="") as file:
            columns = ["country", "town"]
            writer = csv.DictWriter(file, fieldnames=columns)

            # запись заголовка - строка с именами ключей
            writer.writeheader()

            for country,town in func.countries.items():
                # собственно запись в файл writerow()
                writer.writerow({"country":country, "town":town})
        # end with
        input(f"Press Any Key....")
        print()

    except Exception:
        print("Общее исключение")

def task4(file_name):
    try:
        pass
        print(f'Read from File dictionary')
        # чтение словаря из файла
        with open(sys.path[0] + "\\" + file_name, "r", newline="", encoding='UTF=8') as file:
            reader = csv.DictReader(file)

            # чтение и вывод данных, не обязательно выводить все поля
            # сохранение прочитанных данных в коллекции
            func.countries = dict()
            for row in reader:
                print(f'{row["country"]} - {row["town"]}')
                func.countries.update({row["country"]:row["town"]})
        # end with
        input(f"Press Any Key....")
        print()

    except Exception:
        print("Общее исключение")
    
def task5():
    try:
        pass
        print(f'Add New Country and Town')
        country = input("Введите страну: ")
        town = input("Введите город: ")
     
        func.countries.update({country:town})
        print()

        print("Обновленный словарь")
        for country,town in func.countries.items():
             print(f"{country}:{town}")
        print()
        input(f"Press Any Key....")
        print()

    except Exception:
        print("Общее исключение")


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from MainHomeWork003 import main
    main()
# end if