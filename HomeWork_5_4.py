from googletrans import Translator

trans = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as file:
    text = [i.split() for i in file.readlines()]

for i in text:
    result = trans.translate(i[0], src='en', dest='ru')
    i.insert(0, result.text)
    i.remove(i[1])

with open('text_4_1.txt', 'w', encoding='utf-8') as file_save:
    text = [' '.join(i) + '\n' for i in text]
    file_save.writelines(text)
print(text)