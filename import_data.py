def import_data(data, sep=';'):
    with open('phone_book.csv', 'a+') as file:
        if sep == ' ':
            for i in data:
                file.write(f'{i}')
            file.write(f'{i}')
        else:
            file.write(sep.join(data))
            file.write(f'\n')