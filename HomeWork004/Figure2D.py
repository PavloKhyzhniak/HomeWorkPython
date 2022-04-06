# вспомогательные функции задания
import shelve

# базовый класс иерархии
class Figure2D:
    # методы класса
    # конструктор
    def __init__(self, side):
        self.__side = side
        self.__name = 'figure2d'

    # end __init__
    @property
    def _name(self):
        return self.__name
    # end

    @_name.setter
    def _name(self, name):
        if len(name) > 0:
            self.__name = name
        # end if
    # end

    @property
    def side(self):
        return self.__side
    # end

    @side.setter
    def side(self, side):
        if side > 0:
            self.__side = side
        # end if
    # end

    def area(self):
        pass

    def perimeter(self):
        pass


    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        return f'сторона  {self.__side}'
    # end __str__

    # статический атрибут класса - заголовок таблицы
    to_table_header = \
        '\t┌─────┬──────────────────────────┬──────────────────────────┬──────────────────────────┬──────────────────────────┐\n'\
        '\t│  №  │ имя                      │ сторона                  │ площадь                  │ периметр                 │\n'\
        '\t│ п/п │                          │                          │                          │                          │\n'\
        '\t├─────┼──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤'

    # статический атрибут класса - подвал таблицы
    to_table_footer = \
        '\t└─────┴──────────────────────────┴──────────────────────────┴──────────────────────────┴──────────────────────────┘'

    # вывод объекта в виде строки таблицы
    def to_table_row(self, i):
        # сформировать и вернуть строку таблицы
        return f'\t│ {i:3} │ {self.__name:24} │ {self.__side:24} │ {self.area():24} │ {self.perimeter():24} │'
    # end to_table_row

    # выводим список товаров в табличном формате
    def show_list(title, data):
        # вывод заголовка таблицы товаров
        # обращение к статическому атрибуту класса - header
        print(f'\t\t\033[30;1m{title}\n{Figure2D.to_table_header}')

        # вывод основной части таблицы товаров
        i = 1
        for item in data:
            print(f'{item.to_table_row(i)}')
            i += 1

        # вывод подвала таблицы товаров - обращение к статическому атрибуту класса
        print(f'{Figure2D.to_table_footer}\033[0m\n')
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

