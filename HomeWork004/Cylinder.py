from math import pi, sqrt
from Figure3D import Figure3D

# базовый класс иерархии
class Cylinder(Figure3D):
    # методы класса
    # конструктор
    def __init__(self, side, radius):
        Figure3D.__init__(self, side,radius)          # унаследованный класс
        self._name = 'cylinder'
    # end __init__

    def area(self):
        pass
        return 2*pi*self.radius*(self.side*self.radius)

    def volume(self):
        pass
        return pi*self.radius*self.radius*self.side
        
# end class

