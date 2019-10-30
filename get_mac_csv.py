import csv


def get_mac_csv():
    mac_dict = {}
    filename = 'room1_mac.csv'
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            mac_dict[row[0]] = {"port": row[1], "room": filename}
    return mac_dict


if __name__ == '__main__':
    print(get_mac_csv())
