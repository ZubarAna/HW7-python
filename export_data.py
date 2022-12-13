def export_data():
    with open('phone_book.csv', 'r') as file:
        data = []
        for line in file:
            data.append(line)
    return data