def import_data(data, sep = None):
    with open('phone_book.csv', 'a+') as file:
        if sep == ' ':
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")