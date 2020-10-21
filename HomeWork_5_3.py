with open('text_3.txt', 'r', encoding='utf-8') as file:
    result = [i.replace("\n", "").split() for i in file.readlines()]
print(result)
names = []
average = 0
for i in result:
    if float(i[1]) < 20000:
        names.append(i[0])
    average += float(i[1])
average = average / len(result)
print(f'Workers who receive less 20000 ({names}), and their average salary: {average:.3f}')
