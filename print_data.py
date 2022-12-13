def print_data(data):
    if len(data) > 0:
        print('|', 'Фамилия'.center(10), '|', 'Имя'.center(10), '|', 'Телефон'.center(12), '|', 'Примечание'.center(10), '|')
        print("-" * 42)
        for item in data:
            print('|', item[0].center(10), '|', item[1].center(10), '|', item[2].center(12), '|', item[3].center(10), '|')
    else:
        print("Справочник пуст!")