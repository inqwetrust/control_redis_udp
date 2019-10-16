import socket


def get_local_ip():
    localip = socket.gethostbyname(socket.gethostname())
    return localip


def get_local_subnet():
    ip = get_local_ip()
    ip_prefix = '_'.join(ip.split('.')[:3])
    return ip_prefix


if __name__ == '__main__':
    print(get_local_ip())
    print(get_local_subnet())
