import datetime
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
last_state_dict = current_state_dict.get_current_state_dict()
local_state_dict = last_state_dict
print(local_state_dict)
time_moved = datetime.datetime.now()
udp_recv_count = 0

while True:
    state_dict = current_state_dict.get_current_state_dict()
    change_result = current_state_dict.compare_state_dict(last_state_dict, state_dict)
    if change_result["get_cursor_pos"] == False and state_dict["key_caplock_on"]:  # action
        if datetime.datetime.now() > time_moved:
            print("mouse moved", state_dict["get_cursor_pos"])
            time_moved = datetime.datetime.now() + datetime.timedelta(seconds=1)
        else:
            state_dict["get_cursor_pos"] = last_state_dict["get_cursor_pos"]
    elif change_result["key_caplock_on"] == False:  # action
        print("CAPSLOCK:", state_dict["key_caplock_on"])
    elif change_result["key_scrolllock_on"] == False:  # action
        print("Left Click:", state_dict["key_scrolllock_on"])
        if state_dict["key_scrolllock_on"]:
            print("SEND MOUSE DOWN")
        else:
            print("SEND MOUSE UP")
    elif change_result["key_numlock_on"] == False:  # action
        print("Right Click:", state_dict["key_numlock_on"])
        if state_dict["key_numlock_on"]:
            print("SEND MOUSE DOWN (Right)")
        else:
            print("SEND MOUSE UP (Right)")

    elif change_result["get_read_text_line"] == False:  # action
        print("SEND PASTE:", state_dict["get_read_text_line"])
    elif udp_recv_count % 2500 == 0:
        pass
    else:
        last_state_dict = state_dict
        udp_recv_count += 1
        continue
    pickled = pickle.dumps(state_dict)

    # pickle.loads(codecs.decode(pickled.encode(), 'base64')).decode()
    server.sendto(pickled, ('<broadcast>', 37021))

    last_state_dict = state_dict
    udp_recv_count += 1

    # time.sleep(0.7)
