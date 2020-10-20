from json import dump
list_1 = []
result = {}
result_list = []

with open('text_7.txt', 'r', encoding='utf-8') as file:
    while a := file.readline().replace('\n', '').split():
        list_1.append(a)

for i in list_1:
    result.update({f'{i[0]}': int(i[2]) - int(i[3])})

result_list.append(result)
average_profit = [result.get(i) for i in result if result.get(i) > 0]
average_profit = sum(average_profit) / len(average_profit)
average_profit_dict = {'average_profit': average_profit}
result_list.append(average_profit_dict)

with open('text_7.json', 'w', encoding='utf-8') as a:
    dump(result_list, a, indent=4, ensure_ascii=False)