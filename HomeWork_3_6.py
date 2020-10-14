def my_func(string):
    for i in string:
        if 65 < ord(i) < 122:
            continue
        else:
            return 0
    return string.capitalize()


string = input('Input you string: ').split()
new_string =[]
for i in range(len(string)):
    s = my_func(string[i])
    if s == 0:
        continue
    else:
        new_string.append(s)

string = ' '.join(new_string)
print(string)
