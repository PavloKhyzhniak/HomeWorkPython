from math import pi, sqrt
from Figure3D import Figure3D

# базовый класс иерархии
class TrihedralPyramid(Figure3D):
    # методы класса
    # конструктор
    def __init__(self, side, radius):
        Figure3D.__init__(self, side,radius)          # унаследованный класс
        self._name = 'trihedral pyramid'
    # end __init__

    def area(self):
        pass
        return 3*sqrt(3)/4*self.radius*self.radius

    def volume(self):
        pass
        return sqrt(3)/4*self.radius*self.radius*self.side
        
# end class

