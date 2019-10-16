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
    change_result = current_state_dict.compare_state_dict(last_state_dict, state_dict)
    if last_state_dict["get_uuid"] == state_dict["get_uuid"]:
        continue
    if last_state_dict["get_server_ip"] != state_dict["get_server_ip"]:
        continue
    if last_state_dict["get_server_subnet"] != state_dict["get_server_subnet"]:
        continue
    if change_result["get_cursor_pos"] == False:  # action
        print("mouse moved", state_dict["get_cursor_pos"])
    if change_result["get_cursor_pos"] == False:  # action
        print("mouse moved")
    print(change_result)
    last_state_dict = state_dict
