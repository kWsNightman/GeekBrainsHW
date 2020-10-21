with open('text_6.txt', 'r', encoding='utf-8') as file:
    a = [i.split(':') for i in file.readlines()]
result = {}
for key, val in a:
    summa = []
    iteration = 0
    current_numb = []
    for i in val:
        if i.isdigit():
            current_numb.append(i)
            if not val[iteration+1].isdigit():
                summa.append(''.join(current_numb))
                current_numb.clear()
        iteration += 1
    result.update({f'{key}': sum(map(int, summa))})
print(result)