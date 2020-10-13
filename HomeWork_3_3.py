def my_func(arg_a, arg_b, arg_c):
    numbers = [arg_a, arg_b, arg_c]
    numbers.remove(min(numbers))
    return sum(numbers)


def my_func_2(arg_a, arg_b, arg_c):
    numbers = sorted([arg_a, arg_b, arg_c], reverse=True)
    return sum(numbers[:2])


print(my_func(14, 3, 4))
print(my_func_2(14, 3, 4))
