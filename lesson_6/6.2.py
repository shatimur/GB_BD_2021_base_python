class Road:
    _mass_on_square_m = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, thikness):

        print(f'Для этой дороги нужно {self._length * self._width * Road._mass_on_square_m * thikness * 0.001} '
              f'тонн асфальта')

magadan = Road(5000, 20)
magadan.mass(5)