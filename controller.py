# основная программа, обрабатывает логику
from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
def say_hello():
    print('Здравствуйте!')

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона (шаблон: +7xxxxxxxxxx): ")
    comment = input("Введите комментарий: ")
    return [last_name, first_name, phone_number, comment]

def to_do():
    print('Что вы хотите сделать?\n\
          1 - Ввести новые данные\n\
          2 - Вывести данные\n\
          3 - Поиск контакта')
    c = input('Введите число: ')
    if c == 1:
        import_data(input_data(), sep=' ')
    elif c == 2:
         data = export_data()
         print_data(data)
    else:
        word = input('Кого ищем?\n')
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print('|', 'Фамилия'.center(10), '|', 'Имя'.center(10), '|', 'Телефон'.center(12), '|', 'Примечание'.center(10), '|')
            print("-" * 42)
            print('|', item[0].center(10), '|', item[1].center(10), '|', item[2].center(12), '|', item[3].center(10), '|')
        else:
            print('Нет такого контакта')