def export_data():
    with open('phone_book.csv', 'r') as file:
        data = []
        for line in file:
            if ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
    return data