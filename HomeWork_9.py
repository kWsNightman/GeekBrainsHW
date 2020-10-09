list_mounts = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December'
               ]

dict_mounts = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
               8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
               }

while True:
    user_mounts = input('Input number of mounts: ')
    if user_mounts.isdigit() and 0 < int(user_mounts) <= 12:
        print(f'From list mounts {list_mounts[int(user_mounts) - 1]}')
        print(f'Dict dict mounts {dict_mounts.get(int(user_mounts))}')
        if int(user_mounts) <= 2 or int(user_mounts) == 12:
            print('Winter')
        elif 2 < int(user_mounts) <= 5:
            print('It is a spring')
        elif 5 < int(user_mounts) <= 8:
            print('SUMMER!')
        else:
            print('Fall')
        break
    elif user_mounts.isalpha():
        print('This is not a number!')
        continue
    elif not float(user_mounts).is_integer():
        print('Not a integer number!')
        continue
    elif int(float(user_mounts)) < 0:
        print('Negative number!')
        continue
    else:
        print('Your number is too large!')
        continue
