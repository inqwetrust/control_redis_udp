import csv

pc_remarks_dict = {}


def read_file(filename):
    with open(filename, 'rb') as csv_file:
        csv_file = csv_file.read().decode('utf-16')
    csv_file = csv_file.split('\n')
    for line in csv_file:
        items = line.split('\t')
        if len(items) <= 1:
            continue
        room = items[0]
        port = items[1]
        remarks = [r.replace('\r', '') for r in items[2:]]
        pc_remarks_dict[room + '_' + port] = {'remarks': remarks}
    pass


def get_pc_remarks_csv():
    filename = 'pc_remarks.txt'
    read_file(filename)
    return pc_remarks_dict


if __name__ == '__main__':
    print(get_pc_remarks_csv())
