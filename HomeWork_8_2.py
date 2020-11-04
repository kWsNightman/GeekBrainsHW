class MyZero(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        a, b = int(input('Input a number 1: ')), int(input('Input a number 2: '))
        if b == 0:
            raise MyZero('Cannot be divided by zero')
        print(a / b)
    except MyZero as err:
        print(err)
    except ValueError:
        print('Not a number!!!')
