print('-' * 40)
print(f'Welcome to warehouse')
print('-' * 40)
print('Choose Acton.\n Type "add" for new entree.\n '
      'Type "statistic" to load statistic.\n Type "data" to see the entrees list.\n '
      'Type "exit" to quit')
product_skeleton = {'Name': None, 'Price': 0, 'Quantity': 0, 'Units': 0}
product = []
count = 0
data_products = []

while True:
    user_selection = input('Int your act : ').lower()
    if user_selection == 'add':
        while True:
            n = input('Input count of entrees: ')
            if n.lstrip('-').isdigit():
                break
            print('It not a number!')
        a = product_skeleton.copy()
        while count < abs(int(n)):
            for i in product_skeleton:
                user_inp = input(f'{i} ')
                if i == 'Price' or i == 'Quantity':
                    while True:
                        if user_inp.isdigit():
                            a[i] = int(user_inp)
                            break
                        else:
                            print('It is not a number or not a positive number')
                            user_inp = input(f'{i} ')
                else:
                    a[i] = user_inp
            count += 1
            product.append(count)
            product.append(a)
            data_products.append(tuple(product))
            product.clear()
            print(data_products)
    elif user_selection == 'statistic':
        info = {'Name': [], 'Price': [], 'Quantity': [], 'Units': []}
        for i, val in data_products:
            for b in val:
                info[b].append(val.get(b))
        print(info)
    elif user_selection == 'data':
        print(data_products)
    elif user_selection == 'exit':
        break
    else:
        print('Choose Acton.\n Type "add" for new entree.\n '
              'Type "statistic" to load statistic.\n Type "data" to see the entrees list.\n '
              'Type "exit" to quit')
print('Program end!')
