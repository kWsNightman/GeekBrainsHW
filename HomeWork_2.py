
while True:
    seconds_number = int(input("Hello! Enter your number of seconds, we will convert them to the format hh.mm.ss: "))
    if seconds_number > 86400:
        print('Sorry your number of seconds more than a day, not more 86400')
    elif seconds_number < 0:
        print('The number of seconds cannot be less than zero')
    else:
        hours = seconds_number // 3600
        minutes = (seconds_number % 3600) // 60
        seconds = seconds_number - ((hours * 3600) + (minutes * 60))
        print(f'{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}')
        break



