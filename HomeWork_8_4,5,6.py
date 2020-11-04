def correct_input(checked, of):
    """Проверка число ли в строке"""
    while True:
        if checked == 'q':
            return 'q'
        try:
            checked = int(checked)
            if checked < 0:
                print("Not a negative number!!!")
                checked = input(f'Input a number of {of}:')
                continue
        except ValueError:
            print(f'ERROR! You input not a number! {checked}')
            checked = input(f'Input a number of {of}:')
        else:
            break
    return checked


def create_name(name, obj):
    """Проверка названия при встрече повторного прибовляется нумерация"""
    counts = sum([(''.join(s[1]).count(f'{name}_{obj}_')) for v in w.all_teh.items() for s in v[1].items()])
    return counts + 1


def menu():
    print(
        f'All obj storage: {" ".join(w.all_teh["storage"].get("Printer"))} {" ".join(w.all_teh["storage"].get("Scanner"))} '
        f'{" ".join(w.all_teh["storage"].get("Xerox"))}\noffice: {" ".join(w.all_teh["office"].get("Printer"))} '
        f'{" ".join(w.all_teh["office"].get("Scanner"))} {" ".join(w.all_teh["office"].get("Xerox"))}\n'
        f'broken: {" ".join(w.all_teh["broken"].get("Printer"))} {" ".join(w.all_teh["broken"].get("Scanner"))} '
        f'{" ".join(w.all_teh["broken"].get("Xerox"))}')


def bio(obj):
    if obj.class_teh == 'Printer':
        return f'Name object {obj.model} his cost {obj.price} his paint supplies {obj.paint_consumption}ml ' \
               f'his waste of paint on a sheet {paint_list}ml his status {obj.status}'
    elif obj.class_teh == "Scanner":
        return f'Name object {obj.model} his cost {obj.price} his status {obj.status} '
    elif obj.class_teh == "Xerox":
        return f'Name object {obj.model} his cost {obj.price} his paint supplies {obj.paint_consumption}ml ' \
               f'his waste of paint on a sheet {paint_list}ml his status {obj.status}'


class Warehouse:
    all_teh = {'storage': {'Printer': [], 'Scanner': [], 'Xerox': []},
               'office': {'Printer': [], 'Scanner': [], 'Xerox': []},
               'broken': {'Printer': [], 'Scanner': [], 'Xerox': []}}

    def add_teh(self, obj, to='storage'):
        self.all_teh[to][obj.class_teh].append(obj.model)
        obj.status = to

    def move(self, obj, to):
        try:
            obj = globals().get(obj.capitalize())
        except Exception:
            pass
        else:
            if obj == None:
                print("Obj not found")
            elif obj.status == to:
                print(f'Object in {to}')
            else:
                self.all_teh[obj.status][obj.class_teh].remove(obj.model)
                self.all_teh[to][obj.class_teh].append(obj.model)
                obj.status = to
                print(f'Obj {obj.model} move to {to}')

    def delete_obj(self, obj):
        obj = globals().get(obj.capitalize())
        self.all_teh[obj.status][obj.class_teh].remove(obj.model)
        obj.status = (r'deleted')
        print(f"Obj {obj.model} remove")


class OfficeEquipment:

    def __init__(self, model, price, status="storage"):
        self.model = model
        self.price = price
        self.status = status


class Printer(OfficeEquipment):
    __class_teh = 'Printer'

    def __init__(self, model, price, paint_consumption, paint_list):
        super().__init__(model, price, status="storage")
        self.paint_consumption = paint_consumption
        self.paint_list = paint_list

    @property
    def class_teh(self):
        return Printer.__class_teh


class Scanner(OfficeEquipment):
    __class_teh = 'Scanner'

    def __init__(self, model, price, all_lists=0):
        super().__init__(model, price, status="storage")
        self.__all_list = all_lists

    @property
    def class_teh(self):
        return Scanner.__class_teh

    def scan_list(self, numbers):
        self.__all_list += numbers

    @property
    def all_list(self):
        return self.__all_list


class Xerox(OfficeEquipment):
    __class_teh = "Xerox"

    def __init__(self, model, price, paint_consumption, paint_list):
        super().__init__(model, price, status="storage")
        self.paint_consumption = paint_consumption
        self.paint_list = paint_list

    @property
    def class_teh(self):
        return Xerox.__class_teh


w = Warehouse()
Asus_printer_1 = Printer("Asus_printer_1", 123, 100, 1)
Hp_scanner_1 = Scanner('Hp_scanner_1', 132)
print(type(Asus_printer_1))
print(type(Asus_printer_1.model))
Hp_scanner_1.scan_list(2)
Hp_scanner_1.scan_list(14)
print(Hp_scanner_1.all_list)
w.add_teh(Asus_printer_1, 'storage')
w.add_teh(Hp_scanner_1)
print(w.all_teh)
print(Asus_printer_1.status)
w.move(Asus_printer_1, 'office')
w.move(Asus_printer_1, 'storage')

print(w.all_teh)
while True:
    print('-' * 90, '\n',
          'Menu\nInput 1 for create object\nInput 2 for options with objects\nInput 3 for move/remove obj\nTo exit "q"\n',
          '-' * 90)
    user_choice = correct_input(input('Your choice: '), 'choice in menu')
    if user_choice == 1:
        print('-' * 90, '\n', 'Menu\nInput 1 for create object Printer\nInput 2 for create object Scanner\n'
                              'Input 3 for create object Xerox\n', '-' * 90)
        user_choice_1 = correct_input(input('Your choice: '), 'choice in menu')
        if user_choice_1 == 1:
            name = input('Input model a printer: ').capitalize()
            price = correct_input(input('Input a price: '), 'price')
            paint_consumption = correct_input(input('Input a paint tank volume: '), 'paint tank volume')
            paint_list = correct_input(input('Paint consumption per sheet: '), 'Paint consumption per sheet')
            numbers = correct_input(input('Numbers of created: '), 'number created')
            for _ in range(int(numbers)):
                name_objc = f'{name}_printer_{create_name(name, "printer")}'
                globals()[name_objc] = Printer(model=name_objc, price=price,
                                               paint_consumption=paint_consumption,
                                               paint_list=paint_list)
                w.add_teh(globals()[name_objc])
        elif user_choice_1 == 2:
            name = input('Input model a scanner: ').capitalize()
            price = correct_input(input('Input a price: '), 'price')
            numbers = correct_input(input('Numbers of created: '), 'number created')
            for _ in range(int(numbers)):
                name_objc = f'{name}_scanner_{create_name(name, "scanner")}'
                globals()[name_objc] = Scanner(model=name_objc, price=price)
                w.add_teh(globals()[name_objc])
        elif user_choice_1 == 3:
            name = input('Input model a xerox: ').capitalize()
            price = correct_input(input('Input a price: '), 'price')
            paint_consumption = correct_input(input('Input a paint tank volume: '), 'paint tank volume')
            paint_list = correct_input(input('Paint consumption per sheet: '), 'Paint consumption per sheet')
            numbers = correct_input(input('Numbers of created: '), 'number created')
            for _ in range(int(numbers)):
                name_objc = f'{name}_xerox_{create_name(name, "xerox")}'
                globals()[name_objc] = Xerox(model=name_objc, price=price,
                                             paint_consumption=paint_consumption,
                                             paint_list=paint_list)
                w.add_teh(globals()[name_objc])
        else:
            print("You have not chosen from the menu")
    elif user_choice == 2:
        print('-' * 90, '\n',
              'Menu\nInput 1 for number of storage\nInput 2 for number office\n'
              'Input 3 for number broken\nInput 4 for info obj\n',
              '-' * 90)
        user_choice = correct_input(input('Your choice: '), 'choice in menu')
        if user_choice == 1:
            print(
                f'On storage\nPrinters: {len(w.all_teh["storage"].get("Printer"))}\n'
                f'Scanners: {len(w.all_teh["storage"].get("Scanner"))}\n'
                f'Xeroxes: {len(w.all_teh["storage"].get("Xerox"))}')
        elif user_choice == 2:
            print(
                f'On office\nPrinters: {len(w.all_teh["office"].get("Printer"))}\n'
                f'Scanners: {len(w.all_teh["office"].get("Scanner"))}\n'
                f'Xeroxes: {len(w.all_teh["office"].get("Xerox"))}')
        elif user_choice == 3:
            print(
                f'On broken\nPrinters: {len(w.all_teh["broken"].get("Printer"))}\n'
                f'Scanners: {len(w.all_teh["broken"].get("Scanner"))}\n'
                f'Xeroxes: {len(w.all_teh["broken"].get("Xerox"))}')
        elif user_choice == 4:
            menu()
            user_choice = input('Input a object ')
            print(bio(globals().get(user_choice.capitalize())))
        else:
            print("You have not chosen from the menu")
    elif user_choice == 3:
        print('-' * 90, '\n',
              'Menu\nInput 1 for move object\nInput 2 for remove objects\nInput 3 for list all objects\n',
              '-' * 90)
        user_choice = correct_input(input('Your choice: '), 'choice in menu')
        if user_choice == 1:
            menu()
            obj = input("Input move object: ")
            to = correct_input(input('Input move to 1-Storage 2-Office 3-Broken: '), "move obj")
            if to == 1:
                to = 'storage'
                w.move(obj, to)
            elif to == 2:
                to = 'office'
                w.move(obj, to)
            elif to == 3:
                to = 'broken'
                w.move(obj, to)
            else:
                print("You have not chosen from the menu")
        elif user_choice == 2:
            menu()
            obj = input("input obj: ")
            w.delete_obj(obj)
        elif user_choice == 3:
            print('-' * 90, '\n',
                  'Menu\nInput 1 for list storage\nInput 2 for list office\nInput 3 for list broken\n',
                  '-' * 90)
            user_choice = correct_input(input('Your choice: '), 'choice in menu')
            if user_choice == 1:
                print(
                    f'Printer of storage {w.all_teh["storage"].get("Printer")}\n'
                    f'Scanner {w.all_teh["storage"].get("Scanner")}\nXerox {w.all_teh["storage"].get("Xerox")}')
            elif user_choice == 2:
                print(
                    f'Printer of office {w.all_teh["office"].get("Printer")}\n'
                    f'Scanner {w.all_teh["office"].get("Scanner")}\nXerox {w.all_teh["office"].get("Xerox")}')
            elif user_choice == 3:
                print(
                    f'Printer of broken {w.all_teh["broken"].get("Printer")}\n'
                    f'Scanner {w.all_teh["broken"].get("Scanner")}\nXerox {w.all_teh["broken"].get("Xerox")}')
            else:
                print("You have not chosen from the menu")
    elif user_choice.lower() == 'q':
        break
print("Program closed")
