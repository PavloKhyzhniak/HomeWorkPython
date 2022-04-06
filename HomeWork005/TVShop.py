# вспомогательные функции задания
import shelve
from TVShopType import TVShopType
from TVShopManufacturer import TVShopManufacturer

# базовый класс иерархии
class TVShop:
    # методы класса
    # конструктор
    def __init__(self, manufacturer, base, name, size, vertical, horizontal, price):
        self.__manufacturer = manufacturer
        self.__type = TVShopType(base, name, manufacturer, size, vertical, horizontal)
        self.__price = price
    # end __init__

    def initialized():
        return [TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KDL_43WF804.jpeg", "Sony_KDL_43WF804", 42.5, 1920, 1080, 11200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KDL_43WG665.jpeg", "Sony_KDL_43WG665", 42.8, 1920, 1080, 1200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KDL_32WD756.jpeg", "Sony_KDL_32WD756", 31.5, 1920, 1080, 1200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_49XH8596.jpeg", "Sony_KD_49XH8596", 48.5, 1920, 1080, 12200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_49XH8096.jpeg", "Sony_KD_49XH8096", 48.5, 3840, 2160, 14200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_55XG7005.jpeg", "Sony_KD_55XG7005", 54.6, 3840, 2160, 15200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_55XH9505.jpeg", "Sony_KD_55XH9505", 54.6, 3840, 2160, 16200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_55XH9096.jpeg", "Sony_KD_55XH9096", 43., 1920, 1080, 17200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_65A8.jpeg", "Sony_KD_65A8", 43., 1920, 1080, 15200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_65AG9.jpeg", "Sony_KD_65AG9", 43., 1920, 1080, 15200)
              , TVShop(TVShopManufacturer.Collection()['Sony'], "Sony_KD_75ZH8.jpeg", "Sony_KD_75ZH8", 75.4, 7680, 4320, 16200)


              , TVShop(TVShopManufacturer.Collection()['LG'], "LG_32LK519B.jpeg", "LG_32LK519B", 32.4, 7680, 4320, 143200)
              , TVShop(TVShopManufacturer.Collection()['LG'], "LG_28TN525S_PZ.jpeg", "LG_28TN525S_PZ", 28.4, 7680, 4320, 12200)
              , TVShop(TVShopManufacturer.Collection()['LG'], "LG_22TN610V_PZ.jpeg", "LG_22TN610V_PZ", 22.4, 7680, 4320, 1200)

              , TVShop(TVShopManufacturer.Collection()['Samsung'], "Samsung_UE32T4510AU.jpeg", "Samsung_UE32T4510AU", 32.4, 7680, 4320, 11200)
              , TVShop(TVShopManufacturer.Collection()['Samsung'], "Samsung_UE43N5500AU.jpeg", "Samsung_UE43N5500AU", 43.4, 7680, 4320, 16200)
              , TVShop(TVShopManufacturer.Collection()['Samsung'], "Samsung_UE43N5000AU.jpeg", "Samsung_UE43N5000AU", 43.4, 7680, 4320, 1200)

              , TVShop(TVShopManufacturer.Collection()['Panasonic'], "TX_58GXR700.jpeg", "TX_58GXR700", 58.4, 7680, 4320, 12400)
              , TVShop(TVShopManufacturer.Collection()['Panasonic'], "TX_32FR250W.jpeg", "TX_32FR250W", 32.4, 7680, 4320, 1200)
              , TVShop(TVShopManufacturer.Collection()['Panasonic'], "TX_65GXR900.jpeg", "TX_65GXR900", 65.4, 7680, 4320, 17200)

              , TVShop(TVShopManufacturer.Collection()['Philips'], "Philips_43PFS5813.jpeg", "Philips_43PFS5813", 43.4, 7680, 4320, 174200)
              , TVShop(TVShopManufacturer.Collection()['Philips'], "Philips_50PUS6704.jpeg", "Philips_50PUS6704", 50.4, 7680, 4320, 1200)
              , TVShop(TVShopManufacturer.Collection()['Philips'], "Philips_65PUS7303.jpeg", "Philips_65PUS7303", 65.4, 7680, 4320, 15200)
        ]

    @property
    def manufacturer(self):
        return self.__manufacturer
    # end 

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
        # end if
    # end 

    @property
    def type(self):
        return self.__type
    # end 

    @type.setter
    def type(self, type):
        self.__type = type
        # end if
    # end 

    @property
    def price(self):
        return self.__price
    # end 

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
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
        return f'type  {self.__type}\
        , price {self.__price:10}'
    # end __str__

    # статический атрибут класса - заголовок таблицы
    to_table_header = \
        '\t┌─────┬──────────────────────────┬──────────────────────────┬──────────────┬────────────┬───────────────┬──────────────┐\n'\
        '\t│  №  │ Manufacturer             │ Type                     │   Size       │ Vertical   │ Horizontal    │ Price        │\n'\
        '\t│ п/п │                          │                          │              │            │               │              │\n'\
        '\t│     │                          │                          │              │            │               │              │\n'\
        '\t├─────┼──────────────────────────┼──────────────────────────┼──────────────┼────────────┼───────────────┼──────────────┤'

    # статический атрибут класса - подвал таблицы
    to_table_footer = \
        '\t└─────┴──────────────────────────┴──────────────────────────┴──────────────┴────────────┴───────────────┴──────────────┘'

    # вывод объекта в виде строки таблицы
    def to_table_row(self, i):
        # сформировать и вернуть строку таблицы
        return f'\t│ {i:3} │ {self.manufacturer.name:24} │ {self.type.name:24} │ {self.type.size:12} │ {self.type.vertical:10} │ {self.type.horizontal:13} │ {self.price:12} │'
    # end to_table_row

    # выводим список товаров в табличном формате
    def show_list(title, data):
        # вывод заголовка таблицы товаров
        # обращение к статическому атрибуту класса - header
        print(f'\t\t\033[30;1m{title}\n{TVShop.to_table_header}')

        # вывод основной части таблицы товаров
        i = 1
        for item in data:
            print(f'{item.to_table_row(i)}')
            i += 1

        # вывод подвала таблицы товаров - обращение к статическому атрибуту класса
        print(f'{TVShop.to_table_footer}\033[0m\n')
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

