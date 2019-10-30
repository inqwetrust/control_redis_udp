import csv


def get_mac_csv():
    mac_dict = {}
    filename = 'room1_mac.csv'
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            mac = str(row[0])
            mac = mac.replace('-', '')
            print(mac)
            mac = ':'.join([mac[i:i+2] for i,j in enumerate(mac) if not (i%2)])
            mac = mac.upper()
            mac_dict[mac] = {"port": row[1], "room": filename}
    return mac_dict


if __name__ == '__main__':
    print(get_mac_csv())
