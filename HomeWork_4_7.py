def fact(number):
    result = 1
    if number == 0:
        yield 1
    for i in range(number):
        result = result * (i + 1)
        yield result


n = int(input('Enter the number: '))
numbers = []
count = 0
result = 0
for i in fact(n):
    if n == 0:
        result = i
        numbers.append(0)
    if count + 1 == n:
        result = i
    numbers.append(count + 1)
    count += 1
string = '*'.join(map(str, numbers))
print(f'Factorial {n}!={string}={result}')
