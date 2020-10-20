numbers_rus = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
with open('text_4.txt', 'r', encoding='utf-8') as file:
    text = [i.split() for i in file.readlines()]

for i in text:
    i.insert(0, numbers_rus.get(i[2]))
    i.remove(i[1])

with open('text_4_1.txt', 'w', encoding='utf-8') as file_save:
    text = [' '.join(i) + '\n' for i in text]
    file_save.writelines(text)
