class ComplexNumber:
    def __init__(self, number):
        self.number = number
        print(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


a_1 = ComplexNumber(complex(3, 3))
a_2 = ComplexNumber(complex(1, 2))
print(a_1 + a_2)
print(a_1 * a_2)
