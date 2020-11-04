class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers = []

while True:
    try:
        a = input('Input a number: ')
        if a.lstrip('-').isdigit():
            numbers.append(int(a))
        elif a.lstrip('-').replace('.', '', 1).isdigit():
            numbers.append(float(a))
        elif a.lower() == 'stop':
            break
        else:
            raise NotNumber('ERROR Not a number!!!')
    except NotNumber as err:
        print(err)
print(numbers)
