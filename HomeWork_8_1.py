import re


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return '{0[0]:02d}-{0[1]:02d}-{0[2]}'.format(Date.valid_date(self.date))

    @classmethod
    def integer_date(cls, date):
        try:
            return [abs(int(i)) for i in re.split("[-:.]", date)]
        except ValueError:
            print('Not a number!!!')

    @staticmethod
    def valid_date(data):
        b = Date.integer_date(data)
        if b[1] > 12:
            b.remove(b[1])
            b.insert(1, 1)
        if b[0] > 31 and b[1] in [1, 3, 5, 7, 8, 10, 12]:
            b.remove(b[0])
            b.insert(0, 31)
        elif b[0] > 30 and b[1] in [4, 6, 9, 11]:
            b.remove(b[0])
            b.insert(0, 30)
        elif b[0] > 30 and b[1] == 2:
            if b[2] // 4 == 0:
                b.remove(b[0])
                b.insert(0, 29)
            else:
                b.remove(b[0])
                b.insert(0, 28)
        if b[2] > 9999:
            b.remove(b[2])
            b.insert(2, 9999)
        return b


d = Date('3 .054:  1995')
print(d)
d_2 = Date('123 - 11 - 1444')
print(d_2)
