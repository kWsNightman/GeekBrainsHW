from functools import reduce

result = reduce(lambda a, b: a * b, [i for i in range(100, 1001) if i % 2 == 0])
print(result)
