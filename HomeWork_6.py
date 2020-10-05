a = 2
b = 4
days = 1
while a < b:
    print(f'Day {days} ran {a:.2f} km')
    a = a + (a * 0.1)
    days += 1
else:
    print(f'On {days} day you will reach the goal of {a:.0f} km')
