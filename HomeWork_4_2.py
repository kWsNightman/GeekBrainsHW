from random import randint
lst = [randint(0, 150) for i in range(15)]
result = [lst[i] for i in range(1, len(lst)) if int(lst[i]) > int(lst[i - 1])]
print(lst)
print(result)
