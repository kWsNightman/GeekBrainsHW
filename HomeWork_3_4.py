def my_func(x, y):
    print(x**y)


def my_func_2(x, y):
    c = x
    if y < 0:
        for i in range(abs(y) - 1):
            c = c*x
        print(1/c)


my_func(5, -2)
my_func_2(5, -2)
