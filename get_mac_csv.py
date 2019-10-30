import csv

mac_dict = {}


def read_file(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            mac = str(row[0])
            mac = mac.replace('-', '')
            mac = ':'.join([mac[i:i + 2] for i, j in enumerate(mac) if not (i % 2)])
            mac = mac.upper()
            port = row[1]
            port = port.split('/')
            port = port[-1]
            mac_dict[mac] = {"room": filename[:5], "port": port}
    pass


def get_mac_csv():
    filename = 'room1_mac.csv'
    read_file(filename)
    filename = 'room2_mac.csv'
    read_file(filename)
    return mac_dict


if __name__ == '__main__':
    print(get_mac_csv())
