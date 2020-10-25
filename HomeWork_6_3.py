class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'.title()

    def get_total_income(self):
        try:
            print(f'Total income: {int(self._income.get("wage")) + int(self._income.get("bonus"))}'
                  f' of worker: {self.get_full_name()}')
        except ValueError:
            print('Not a number wage or bonus!!!')


worker_1 = Position(
    input('Input name: '), input('Input surname: '),
    input('Input employee position: ').capitalize(), {'wage': input('Input wage: '), 'bonus': input('Input bonus: ')}
    )
worker_1.get_full_name()
worker_1.get_total_income()
print(worker_1.position)
