from abc import ABC, abstractmethod


class AbstractClothing(ABC):
    _cloth = [[], []]

    @abstractmethod
    def tissue_consumption(self):
        pass

    @property
    def whole_fabric(self):
        if not AbstractClothing._cloth[1]:
            return f'Total tissue wasted {round(sum([sum(i) for i in AbstractClothing._cloth]), 2)} for ' \
                   f'{len(AbstractClothing._cloth[0])} coat(s) '
        if not AbstractClothing._cloth[0]:
            return f'Total tissue wasted {round(sum([sum(i) for i in AbstractClothing._cloth]), 2)} for ' \
                   f'{len(AbstractClothing._cloth[1])} jacket(s)'
        else:
            return f'Total tissue wasted {round(sum([sum(i) for i in AbstractClothing._cloth]), 2)} for ' \
                   f'{len(AbstractClothing._cloth[0])} coat(s) and for {len(AbstractClothing._cloth[1])} jacket(s)'


class Coat(AbstractClothing):
    __cloth = 0

    def __init__(self, V):
        self.V = V
        self.a = self.V / 6.5 + 0.5
        Coat.__cloth += self.a
        AbstractClothing._cloth[0].append(self.a)

    @property
    def tissue_consumption(self):
        return f'The fabric is gone for the coat with size {self.V} - {round(self.a, 2)}'

    @property
    def cloth_coats(self):
        return f'The fabric is gone for the all coats: {round(Coat.__cloth, 2)} '


class Jacket(AbstractClothing):
    __cloth = 0

    def __init__(self, H):
        self.H = H
        self.a = 2 * self.H + 0.3
        Jacket.__cloth += self.a
        AbstractClothing._cloth[1].append(self.a)

    @property
    def tissue_consumption(self):
        return f'The fabric is gone for the jacket with height {self.H} - {self.a}'

    @property
    def cloth_jackets(self):
        return f'The fabric is gone for the all jackets: {round(Jacket.__cloth, 2)} '


coat_1 = Coat(146)
coat_2 = Coat(156)
print(coat_1.tissue_consumption)
print(coat_2.cloth_coats)
print(coat_1.whole_fabric)
jacket_1 = Jacket(68)
jacket_2 = Jacket(54)
print(jacket_1.tissue_consumption)
print(jacket_2.cloth_jackets)
print(jacket_2.whole_fabric)
