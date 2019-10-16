import uuid


def get_mac_addr():
    mac = uuid.getnode()
    mac = ':'.join(("%012X" % mac)[i:i + 2] for i in range(0, 12, 2))
    return mac


if __name__ == '__main__':
    print(get_mac_addr())
