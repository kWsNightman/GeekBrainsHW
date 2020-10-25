from time import sleep
import colorama
from itertools import cycle
import tkinter as tk

colorama.init()


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        while True:
            print(f'{colorama.Fore.RED + TrafficLight.__color[0]}')
            sleep(7)
            print(f'{colorama.Fore.YELLOW + TrafficLight.__color[1]}')
            sleep(2)
            print(f'{colorama.Fore.GREEN + TrafficLight.__color[2]}')
            sleep(5)
            print(f'{colorama.Fore.YELLOW + TrafficLight.__color[1]}')
            sleep(2)


tr_1 = TrafficLight()
tr_1.running()

# ---------------------------------------------2решение------------------------------------------------------------------
'''В этом решении не совсем по заданию чтобы был один отрибут но по другому я пока что придумать не смог'''


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']
    a_color = cycle([__color[0], __color[0], 'grey', 'grey'])
    b_color = cycle(['grey', __color[1], 'grey', __color[1]])
    c_color = cycle(['grey', 'grey', __color[2], __color[2]])
    timer = cycle([7000, 2000])

    def __init__(self):
        self.root = tk.Tk()
        self.button = tk.Button(self.root, text='Start', command=self.running)
        self.canvas = tk.Canvas(self.root, width=200, height=600, bg='black')

        self.a = self.canvas.create_oval(20, 20, 180, 180, fill='grey')
        self.b = self.canvas.create_oval(20, 200, 180, 360, fill='grey')
        self.c = self.canvas.create_oval(20, 380, 180, 540, fill='grey')
        self.button.pack()
        self.canvas.pack()

        self.root.mainloop()

    def running(self):
        self.a = self.canvas.create_oval(20, 20, 180, 180, fill=next(self.a_color))
        self.b = self.canvas.create_oval(20, 200, 180, 360, fill=next(self.b_color))
        self.c = self.canvas.create_oval(20, 380, 180, 540, fill=next(self.c_color))
        self.canvas.after(next(self.timer), self.running)


tr = TrafficLight()
