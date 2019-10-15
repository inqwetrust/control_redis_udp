import socket

import time
import random
import uuid

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block

# indefinitely when trying to receive data.

server.settimeout(0.2)

server.bind(("", 44444))

message = b"your very important message"

while True:
    hash = uuid.uuid4().hex

    server.sendto(message, ('<broadcast>', 37020))
    server.sendto(str(hash).encode(), ('<broadcast>', 37021))

    print("message sent!")

    time.sleep(1)
