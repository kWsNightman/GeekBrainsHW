class Cell:

    def __init__(self, number):
        self.number = number

        if self.number < 0:
            try:
                raise ValueError
            except ValueError:
                print(f"ERROR !! There cannot be a negative number of cells!!!! {self.number}")

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return (self.number - other.number) if (self.number - other.number) > 0 else other.number - self.number

    def __mul__(self, other):
        return self.number * other.number

    def __floordiv__(self, other):
        return self.number // other.number if self.number // other.number != 0 else other.number // self.number

    def make_order(self, n):
        return '\n'.join(['*' * n for i in range(self.number // n)]) + "\n" + ('*' * (self.number % n))


c_1 = Cell(33)
c_2 = Cell(26)
c_3 = Cell(-3)
print(c_2 + c_1)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
print(c_1.make_order(5))
print(c_2.make_order(3))
