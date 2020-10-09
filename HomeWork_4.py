user_number = int(input('Enter your number: '))
max_number = 0
while user_number != 0:
    current_number = user_number % 10
    if current_number >= max_number:
        max_number = current_number
    user_number = user_number//10
print(max_number)