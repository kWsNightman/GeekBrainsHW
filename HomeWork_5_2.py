with open('zen.txt', 'r', encoding='utf-8') as file:
    strings = 0
    word_of_strings = 0
    while string := file.readline().replace("\n", ""):
        word_of_string = len(string.split())
        strings += 1
        word_of_strings += word_of_string
        print(f"{strings}: In string ({string}) {word_of_string} words")
print(f'All strings {strings}, all words {word_of_strings}')
