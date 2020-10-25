class Road:

    def __init__(self, length, width=20):
        self._length = length
        self._width = width

    def mass(self):
        if int(self._width) < 0 or int(self._length) < 0:
            print("Please positive number !!!")
        else:
            print(f'Asphalt mass on road length:{self._length} m and width:{self._width} sm = '
                  f'{(int(self._length) * int(self._width) * 25 * 5) // 1000} tons')


try:
    rd = Road(int(input('Input the length of road: ')), int(input('Input the width of road: ')))
    rd.mass()
except ValueError:
    print("Error input the number!!!")

