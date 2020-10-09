while True:
    user_number = input('Enter your integer number: ')
    if int(user_number) < 0:
        print('Please enter a positive integer number')
    else:
        print(f'{int(user_number) + int(user_number + user_number) + int(user_number + user_number + user_number)}')
        break
