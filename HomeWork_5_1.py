import os

with open('my_file_1.txt', 'a', encoding='utf-8') as m:
    while True:
        a = input('Input your string: ')
        if not a.split():
            break
        else:
            m.write(f'{a}\n')
print(f'File closed, and save on {os.getcwd()}')