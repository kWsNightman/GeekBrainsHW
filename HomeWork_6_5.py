class Stationary:

    def __init__(self, title='New drawing'):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationary):

    def draw(self):
        print('Start drawing with pen')


class Pencil(Stationary):

    def draw(self):
        print('Start drawing with pencil')


class Handle(Stationary):

    def draw(self):
        print('Start drawing with Handle')


pen = Pen()
print(pen.title)
pen.draw()
pencil = Pencil('My best picture')
print(pencil.title)
pencil.draw()
handle = Handle('Handle draw')
print(handle.title)
handle.draw()
