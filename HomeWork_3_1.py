def my_func(a, b):
    try:
        result = int(a)/int(b)
        return result
    except ZeroDivisionError:
        return "ERROR! Please don't divide by zero"
    except ValueError:
        return "ERROR! You entered not a number"


a = input('Enter the number: ')
b = input('Enter the number by which you will divide: ')
print(round(my_func(a, b), 3))
