import pickle
import socket
import random
import current_state_dict

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
client2.bind(("", 37021))
last_state_dict = current_state_dict.get_current_state_dict()
while True:
    # hash = random.randint(0, 100)

    data, addr = client.recvfrom(10240)
    print("received message:{}".format(data))

    data, addr = client2.recvfrom(10240)
    state_dict = pickle.loads(data)
    print(current_state_dict.compare_state_dict(last_state_dict, state_dict))
    last_state_dict = state_dict
    if len(data) > 1:
        pass
