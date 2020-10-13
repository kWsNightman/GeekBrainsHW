def my_func(string):
    """Так же можно через .title() """
    return string.capitalize()


string = input('Input you string: ').split()
for i in range(len(string)):
    s = my_func(string.pop(i))
    string.insert(i, s)
string = ' '.join(string)
print(string)
