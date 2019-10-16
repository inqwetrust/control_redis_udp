import pickle
import socket
import current_state_dict
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block

# indefinitely when trying to receive data.

server.settimeout(0.2)

server.bind(("", 44444))

message = b"your very important message" * 1

while True:
    pickled = pickle.dumps(current_state_dict.get_current_state_dict())

    # pickle.loads(codecs.decode(pickled.encode(), 'base64')).decode()
    server.sendto(message, ('<broadcast>', 37020))
    server.sendto(pickled, ('<broadcast>', 37021))

    print("message sent!")

    time.sleep(0.7)
