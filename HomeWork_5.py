revenue = int(input('Enter company revenue: '))
costs = int(input('Enter company costs: '))
if revenue > costs:
    print('Congratulations your firm has income')
    profitability = (revenue / costs) * 100
    print(f'Profitability of company = {profitability:.0f}%')
    workers = int(input('Please enter number of workers: '))
    print(f'Profit per worker is: {revenue / workers :.2f}')

else:
    print('Your firm is operating at a loss')
