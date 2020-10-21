from random import randint
with open('my_file_5.txt', 'w', encoding='utf-8') as m:
    numbers = []
    for i in range(10):
        numbers.append(str(randint(0, 100)))
    m.write(' '.join(numbers))
    print(numbers)

with open('my_file_5.txt', 'r', encoding='utf-8') as file:
    numbers_read = map(int, file.readline().split())
print(sum(numbers_read))
