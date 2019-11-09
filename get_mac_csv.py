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

    filename = ['room{}_mac.csv'.format(n) for n in range(1, 6)]
    for file in filename:
        try:
            read_file(file)
        except:
            pass
    return mac_dict


if __name__ == '__main__':
    print(get_mac_csv())
