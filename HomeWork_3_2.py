def human_data(name, surname, birth_year, city, email, phone_number):
    birth_year = correct_input(birth_year)
    phone_number = correct_input(phone_number)
    print(
        f'Hello {name.capitalize()} {surname.capitalize()} you was born in {birth_year} year.'
        f' From {city.capitalize()}, you email {email} and phone number: {phone_number}. All correct?')


def correct_input(checked):
    """Проверка число ли в строке"""
    while True:
        try:
            checked = int(checked)
        except ValueError:
            print(f'ERROR! You input not a number! {checked}')
            checked = input('Input a number :')
        else:
            break
    return checked


human_data(
    name=input('Input you name: '), surname=input('Input surname: '), birth_year=input('Input year of birth: '),
    city=input('Input you city: '), email=input('Input email: '), phone_number=input('Input number of phone: ')
)


# ----------------------------------------------------------------------------------------------------------------------
# Способ через kwargs Получилось не совсем читаемо
def human_data_kwargs(**kwargs):
    return kwargs


human_data_kwargs = human_data_kwargs(
    name=input('Input you name: '), surname=input('Input surname: '), birth_year=input('Input year of birth: '),
    city=input('Input you city: '), email=input('Input email: '), phone_number=input('Input number of phone: ')
)
human_data_kwargs['birth_year'] = correct_input(human_data_kwargs.get('birth_year'))
human_data_kwargs['phone_number'] = correct_input(human_data_kwargs.get('phone_number'))
print(
    f'Hello {human_data_kwargs.get("name").capitalize()} {human_data_kwargs.get("surname").capitalize()} '
    f'you was born in {human_data_kwargs.get("birth_year")} year.'
    f' From {human_data_kwargs.get("city").capitalize()}, you email {human_data_kwargs.get("email")}'
    f' and phone number: {human_data_kwargs.get("phone_number")}. All correct?'
)
