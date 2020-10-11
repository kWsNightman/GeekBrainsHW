number_elements = input('Input amount of elements: ')
elements = []
count = 0
while True:
    if number_elements.isdigit():
        while count < int(number_elements):
            elements.append((input(f'Input {count + 1} element: ')))
            count += 1
        else:
            break
    else:
        number_elements = input('Please input a number: ')

for i in range(0, int(number_elements), 2):
    if i + 1 < len(elements):
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
print(elements)
