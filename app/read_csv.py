import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []       
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def read_csv_1(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []       
        for row in reader:
            iterable = zip(header, row)
            country_dict = dict(iterable)
            data.append(country_dict)
        return data

def read_csv_2(path):
    with open(path, 'r') as csvfile:
        data = csv.DictReader(csvfile, delimiter=',')
        return list(data)

if __name__ == "__main__":
    data = read_csv('./app/data.csv')
    print(data[0])

    data = read_csv_1('./app/data.csv')
    print(data[0])

    data = read_csv_2('./app/data.csv')
    print(data[0])