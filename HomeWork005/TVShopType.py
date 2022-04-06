# вспомогательные функции задания
import os
import shelve

# базовый класс иерархии
class TVShopType:
    # методы класса
    # конструктор
    def __init__(self, base, name, manufacturer, size, vertical, horizontal):
        self.__base = base
        self.__name = name
        self.__manufacturer = manufacturer
        self.__size = size
        self.__vertical = vertical
        self.__horizontal = horizontal
    # end __init__


    @property
    def propCF(self):
        return self.__propCF
    # end 

    @propCF.setter
    def propCF(self, propCF):
        self.__propCF = propCF
        # end if
    # end 

    @property
    def propHDMI(self):
        return self.__propHDMI
    # end 

    @propHDMI.setter
    def propHDMI(self, propHDMI):
        self.__propHDMI = propHDMI
        # end if
    # end 

    @property
    def propUSB(self):
        return self.__propUSB
    # end 

    @propUSB.setter
    def propUSB(self, propUSB):
        self.__propUSB = propUSB
        # end if
    # end 

    @property
    def base(self):
        return os.path.join(os.path.dirname(__file__),"assets\\TVShop\\Type\\"+self.__base)
    # end 

    @base.setter
    def base(self, base):
        if len(base) > 0:
            self.__base = base
        # end if
    # end 

    @property
    def name(self):
        return self.__name
    # end 

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self.__name = name
        # end if
    # end 

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
    def size(self):
        return self.__size
    # end 

    @size.setter
    def size(self, size):
        if size > 0:
            self.__size = size
        # end if
    # end 

    @property
    def vertical(self):
        return self.__vertical
    # end 

    @vertical.setter
    def vertical(self, vertical):
        if vertical > 0:
            self.__vertical = vertical
        # end if
    # end 

    @property
    def horizontal(self):
        return self.__horizontal
    # end 

    @horizontal.setter
    def horizontal(self, horizontal):
        if horizontal > 0:
            self.__horizontal = horizontal
        # end if
    # end 
    
    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        #base, name, manufacturer, size, vertical, horizontal
        return f'base {self.__base:25}\
        , name {self.__name:20}\
        , manufacturer {self.__manufacturer}\
        , size {self.__size:6}\
        , vertical {self.__vertical:6}\
        , horizontal {self.__horizontal:6}'
    # end __str__
    
# end class

