# вспомогательные функции задания
import shelve

# базовый класс иерархии
class Plane:
    # методы класса
    # конструктор
    def __init__(self, aircraftType, countPlace, countPassenger, fuel, countEngines, nameOwner):
        #тип самолета (Ил-76, Boeing-747, …)
        self.__aircraftType = aircraftType
        #количество пассажирских мест (целое число, от 0 и выше)
        self.__countPlace = countPlace
        #текущее количество пассажиров
        self.__countPassenger = countPassenger
        #расход горючего за час полета (вещественное число, от 0 и выше)
        self.__fuel = fuel
        #количество двигателей (целое число, от 1 до 12)
        self.__countEngines = countEngines
        #название авиакомпании – владельца (непустая строка)
        self.__nameOwner = nameOwner
    # end __init__

    @property
    def aircraftType(self):
        return self.__aircraftType
    # end age

    @aircraftType.setter
    def aircraftType(self, aircraftType):
        if len(aircraftType) > 0:
            self.__aircraftType = aircraftType
        # end if
    # end age

    @property
    def countPlace(self):
        return self.__countPlace
    # end city

    @countPlace.setter
    def countPlace(self, countPlace):
        if countPlace > 0:
            self.__countPlace = countPlace
        # end if
    # end city

    @property
    def countPassenger(self):
        return self.__countPassenger
    # end city

    @countPassenger.setter
    def countPassenger(self, countPassenger):
        if countPassenger > 0:
            self.__countPassenger = countPassenger
        # end if
    # end city

    @property
    def fuel(self):
        return self.__fuel
    # end city

    @fuel.setter
    def fuel(self, fuel):
        if fuel > 0:
            self.__fuel = fuel
        # end if
    # end city

    @property
    def countEngines(self):
        return self.__countEngines
    # end city

    @countEngines.setter
    def countEngines(self, countEngines):
        if countEngines > 0:
            self.__countEngines = countEngines
        # end if
    # end city

    @property
    def nameOwner(self):
        return self.__nameOwner
    # end age

    @nameOwner.setter
    def nameOwner(self, nameOwner):
        if len(nameOwner) > 0:
            self.__nameOwner = nameOwner
        # end if
    # end age



    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        #aircraftType, countPlace, countPassenger, fuel, countEngines, nameOwner)
        return f'тип самолета  {self.__aircraftType}\
        , количество пассажирских мест  {self.__countPlace}\
        , текущее количество пассажиров {self.__countPassenger}\
        , расход горючего за час полета {self.__fuel}\
        , количество двигателей {self.__countEngines}\
        , название авиакомпании – владельца {self.__nameOwner}'
    # end __str__

    # статический атрибут класса - заголовок таблицы
    to_table_header = \
        '\t┌─────┬──────────────────────────┬──────────────┬────────────┬───────────────┬──────────────┬──────────────┐\n'\
        '\t│  №  │ тип самолета             │ количество   │ текущее    │ расход        │ количество   │ название     │\n'\
        '\t│ п/п │                          │ пассажирских │ количество │ горючего      │ двигателей   │ авиакомпании │\n'\
        '\t│     │                          │ мест         │ пассажиров │ за час полета │              │ владельца    │\n'\
        '\t├─────┼──────────────────────────┼──────────────┼────────────┼───────────────┼──────────────┼──────────────┤'

    # статический атрибут класса - подвал таблицы
    to_table_footer = \
        '\t└─────┴──────────────────────────┴──────────────┴────────────┴───────────────┴──────────────┴──────────────┘'

    # вывод объекта в виде строки таблицы
    def to_table_row(self, i):
        # сформировать и вернуть строку таблицы
        return f'\t│ {i:3} │ {self.__aircraftType:24} │ {self.__countPlace:12} │ {self.__countPassenger:10} │ {self.__fuel:13} │ {self.__countEngines:12} │ {self.__nameOwner:12} │'
    # end to_table_row

    # выводим список товаров в табличном формате
    def show_list(title, data):
        # вывод заголовка таблицы товаров
        # обращение к статическому атрибуту класса - header
        print(f'\t\t\033[30;1m{title}\n{Plane.to_table_header}')

        # вывод основной части таблицы товаров
        i = 1
        for item in data:
            print(f'{item.to_table_row(i)}')
            i += 1

        # вывод подвала таблицы товаров - обращение к статическому атрибуту класса
        print(f'{Plane.to_table_footer}\033[0m\n')
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

