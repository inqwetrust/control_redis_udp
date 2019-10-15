import socket
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
client2.bind(("", 37021))

while True:
    hash = random.randint(0, 100)

    data, addr = client.recvfrom(10240)
    print("received message:{}{}".format(data, hash))

    data, addr = client2.recvfrom(10240)

    print("received message: %s" % data)
    if len(data) > 1:
        pass
