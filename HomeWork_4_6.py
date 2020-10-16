from itertools import count, cycle, islice

lst = [i for i in islice(count(3), 8)]
iterator = cycle(lst)
print(lst)
print([next(iterator) for i in range(10)])
