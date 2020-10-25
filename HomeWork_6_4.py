from random import choice

direction = ['to the left', 'to the right', 'to turn']


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Auto {self.name} starts moving ')

    def stop(self):
        print(f'The car {self.name} stopped')

    def turn(self, direction):
        print(f'Auto {self.name} going {choice(direction)}')

    def sow_speed(self):
        print(f'Auto speed: {self.speed}')


class TownCar(Car):

    def sow_speed(self):
        if self.speed > 60:
            print(f'You are speeding by: {self.speed - 60}')
        else:
            print(f'Your speed {self.speed}')


class WorkCar(Car):

    def sow_speed(self):
        if self.speed > 40:
            print(f'You are speeding by: {self.speed - 40}')
        else:
            print(f'Your speed {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


car_1 = TownCar('Toyota', 'Green', 70)
print(car_1.name)
print(car_1.speed)
print(car_1.color)
print(car_1.is_police)
car_1.go()
car_1.turn(direction)
car_1.sow_speed()
car_1.stop()

car_2 = WorkCar('Daf', 'White', 40)
print(car_2.name)
print(car_2.speed)
print(car_2.color)
print(car_2.is_police)
car_2.go()
car_2.turn(direction)
car_2.sow_speed()
car_2.stop()

car_3 = SportCar('Ferrari', 'Red', 280)
print(car_3.name)
print(car_3.speed)
print(car_3.color)
print(car_3.is_police)
car_3.go()
car_3.turn(direction)
car_3.sow_speed()
car_3.stop()

car_4 = PoliceCar('Mercedes', 'Black', 100)
print(car_4.name)
print(car_4.speed)
print(car_4.color)
print(car_4.is_police)
car_4.go()
car_4.turn(direction)
car_4.sow_speed()
car_4.stop()
