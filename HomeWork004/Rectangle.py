from math import sqrt
from Figure2D import Figure2D

# базовый класс иерархии
class Rectangle(Figure2D):
    # методы класса
    # конструктор
    def __init__(self, side):
        Figure2D.__init__(self, side)          # унаследованный класс
        self._name = 'rectangle'
    # end __init__

    def area(self):
        pass
        return self.side*self.side

    def perimeter(self):
        pass
        return 4*self.side

# end class

