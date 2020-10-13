def my_func(string):
    numbers = string.split()
    result = []
    n = 1
    for i in range(len(numbers)):
        if numbers[i].lower() == 'q':
            n = 0
            return sum(result), n
        else:
            result.append(correct_input(numbers[i]))
    return sum(result), n


def correct_input(checked):
    """Проверка число ли в строке но обрезает с плавующей точкой """
    while True:
        try:
            checked = int(float(checked))
        except ValueError:
            print(f'ERROR! You input not a number! {checked}')
            checked = input('Replace with number: ')
        else:
            break
    return checked


all_sum = 0
n = 1
while n == 1:
    current_sum, n = my_func(input('Input a numbers: '))
    all_sum = current_sum + all_sum
    print(f'Current sum = {current_sum}, all sum = {all_sum}')
    if n == 1:
        print('For quit input "q"')