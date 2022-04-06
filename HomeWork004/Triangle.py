from math import sqrt
from Figure2D import Figure2D

# базовый класс иерархии
class Triangle(Figure2D):
    # методы класса
    # конструктор
    def __init__(self, side):
        Figure2D.__init__(self, side)          # унаследованный класс
        self._name = 'triangle'
    # end __init__

    def area(self):
        pass
        return sqrt(3)/4*self.side*self.side

    def perimeter(self):
        pass
        return 3*self.side

# end class

