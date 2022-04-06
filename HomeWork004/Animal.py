# вспомогательные функции задания
import shelve

# базовый класс иерархии
class Animal:
    # методы класса
    # конструктор
    def __init__(self, animalNames, weight, age, colors, ownerFirstName, ownerLastName):
        #клички животного, 
        self.__animalNames = animalNames
        #веса (в кг), 
        self.__weight = weight
        #возраста (в полных годах), 
        self.__age = age
        #цвета (масть) животного, 
        self.__colors = colors
        #фамилии и инициалов владельца (Иванов И.И., …).
        self.__ownerFirstName = ownerFirstName
        self.__ownerLastName = ownerLastName
    # end __init__

    @property
    def animalNames(self):
        return self.__animalNames
    # end 

    @animalNames.setter
    def animalNames(self, animalNames):
        if len(animalNames) > 0:
            self.__animalNames = animalNames
        # end if
    # end 

    @property
    def colors(self):
        return self.__colors
    # end 

    @colors.setter
    def colors(self, colors):
        if len(colors) > 0:
            self.__colors = colors
        # end if
    # end 

    @property
    def ownerFirstName(self):
        return self.__ownerFirstName
    # end 

    @ownerFirstName.setter
    def ownerFirstName(self, ownerFirstName):
        if len(ownerFirstName) > 0:
            self.__ownerFirstName = ownerFirstName
        # end if
    # end 

    @property
    def ownerLastName(self):
        return self.__ownerLastName
    # end 

    @ownerLastName.setter
    def ownerLastName(self, ownerLastName):
        if len(ownerLastName) > 0:
            self.__ownerLastName = ownerLastName
        # end if
    # end 

    @property
    def weight(self):
        return self.__weight
    # end 

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        # end if
    # end 

    @property
    def age(self):
        return self.__age
    # end 

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        # end if
    # end 


    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        #aircraftType, countPlace, countPassenger, fuel, countEngines, nameOwner)
        return f'клички животного  {self.__animalNames}\
        , веса (в кг)  {self.__weight}\
        , возраста (в полных годах) {self.__age}\
        , цвета (масть) животного {self.__colors}\
        , фамилии и инициалов владельца {self.__ownerLastName} {self.__ownerFirstName}'
    # end __str__


    # статический атрибут класса - заголовок таблицы
    to_table_header = \
        '\t┌─────┬──────────────────────────┬──────────────┬────────────┬───────────────┬──────────────┬──────────────┐\n'\
        '\t│  №  │ клички животного         │ веса         │ возраста   │ цвета         │ фамилии      │ имя          │\n'\
        '\t│ п/п │                          │ (в кг)       │ (в полных  │ (масть)       │ владельца    │ владельца    │\n'\
        '\t│     │                          │              │ годах)     │ животного     │              │              │\n'\
        '\t├─────┼──────────────────────────┼──────────────┼────────────┼───────────────┼──────────────┼──────────────┤'

    # статический атрибут класса - подвал таблицы
    to_table_footer = \
        '\t└─────┴──────────────────────────┴──────────────┴────────────┴───────────────┴──────────────┴──────────────┘'

    # вывод объекта в виде строки таблицы
    def to_table_row(self, i):
        # сформировать и вернуть строку таблицы
        return f'\t│ {i:3} │ {self.__animalNames:24} │ {self.__weight:12} │ {self.__age:10} │ {self.__colors:13} │ {self.__ownerLastName:12} │ {self.__ownerFirstName:12} │'
    # end to_table_row

    # выводим список товаров в табличном формате
    def show_list(title, data):
        # вывод заголовка таблицы товаров
        # обращение к статическому атрибуту класса - header
        print(f'\t\t\033[30;1m{title}\n{Animal.to_table_header}')

        # вывод основной части таблицы товаров
        i = 1
        for item in data:
            print(f'{item.to_table_row(i)}')
            i += 1

        # вывод подвала таблицы товаров - обращение к статическому атрибуту класса
        print(f'{Animal.to_table_footer}\033[0m\n')
    # end show_list

    # чтение списка из бинарного файла при помощи модуля shelve
    def read_list(file_name):
        data = []
        with shelve.open(file_name) as data_file:
            for datum in data_file:
                data.append(data_file[datum])   # data_file[datum] - собственно чтение
            # end for
        # end with
        return data
    # end read_list

    # запись списка товаров в бинарный файл при помощи модуля shelve
    def write_list(file_name, data):
        # запись файла при помощи модуля shelve
        with shelve.open(file_name) as data_file:
            i = 1
            for datum in data:
                # 'data_file[str(i)] =' вместе с присваиванием это и есть запись в файл
                # ключом словаря в данном случае может быть строка, не может быть int
                data_file[str(i)] = datum
                i += 1
            # end for
        # end with
    # end write_list

# end class

