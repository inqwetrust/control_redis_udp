import csv

pc_remarks_dict = {}


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
            pc_remarks_dict[mac] = {"room": filename[:5], "port": port}
    pass


def get_pc_remarks_csv():
    filename = 'pc_remarks.txt'
    read_file(filename)
    return pc_remarks_dict


if __name__ == '__main__':
    print(get_pc_remarks_csv())
