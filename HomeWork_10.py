count = 0
user_words = input('Input some words: ').split()
for i in user_words:
    if i.isalpha():
        if len(i) > 10:
            print(f'{count + 1}:{i[:11]}')
        else:
            print(f'{count + 1}:{i}')
        count += 1
    else:
        while not i.isalpha():
            print(f'This is not a word {i} please replace')
            user_words.pop(count)
            user_words.insert(count, input())
            i = user_words[count]
        else:
            print(f'{count + 1}:{i}')
            count += 1

