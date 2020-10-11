ratings = [7, 5, 3, 3, 2]
print('If you want to finish enter "exit"')
user_number = input('Input a number: ').lower()
while not user_number == 'exit':
    if user_number.lstrip('-').isdigit():
        if int(user_number) < min(ratings):
            ratings.append(int(user_number))
            print(ratings)
        else:
            for i in ratings:
                if i > int(user_number):
                    continue
                else:
                    ratings.insert(ratings.index(i), int(user_number))
                    print(ratings)
                    break
    else:
        print(f'Is not a number! {user_number}')
    user_number = input('Input a number: ').lower()

