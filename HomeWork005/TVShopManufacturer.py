
# базовый класс иерархии
import os


class TVShopManufacturer():

    # методы класса
    # конструктор
    def __init__(self, filename,name):
        self.__filename = filename
        self.__name = name  
    # end __init__
 

    def init():
        return {
        'Sony' : TVShopManufacturer("Sony.png", "Sony")
        ,'LG' : TVShopManufacturer("LG.png", "LG")
        ,'Samsung' : TVShopManufacturer("Samsung.png", "Samsung")
        ,'Panasonic' : TVShopManufacturer("Panasonic.png", "Panasonic")
        ,'Philips' : TVShopManufacturer("Philips.png", "Philips")
        ,'TLC' : TVShopManufacturer("TLC.png", "TLC")
        ,'Hyundai' : TVShopManufacturer("Hyundai.png", "Hyundai")
        ,'BBKElectronics' : TVShopManufacturer("BBKElectronics.png", "BBKElectronics")
        ,'Supra' : TVShopManufacturer("Supra.png", "Supra")
        ,'Thomson' : TVShopManufacturer("Thomson.png", "Thomson")
        }

    __mycollection=0

    def Collection():
        if(TVShopManufacturer.__mycollection==0):
            TVShopManufacturer.__mycollection = TVShopManufacturer.init()
        return TVShopManufacturer.__mycollection
    # end 


    @property
    def filename(self):
        return os.path.join(os.path.dirname(__file__),"assets\\TVShop\\Manufacturer\\"+self.__filename)
    # end 

    @filename.setter
    def filename(self, filename):
        if len(filename) > 0:
            self.__filename = filename
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
 

    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        #aircraftType, countPlace, countPassenger, fuel, countEngines, nameOwner)
        return f'filename {self.__filename:15}\
        , name {self.__name:15}'
    # end __str__
    
# end class

