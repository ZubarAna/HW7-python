def import_data(data, sep=' '):
    with open('phone_book.csv', 'a+') as file:
        print('Введите данные через пробел: \n\
              Фамилия\n\
              Имя\n\
              Номер_телефона(шаблон: +7xxxxxxxxxx)\n\
              Комментарий')
        if sep == ' ':
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")