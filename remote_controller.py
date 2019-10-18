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

while True:
    state_dict = current_state_dict.get_current_state_dict()
    change_result = current_state_dict.compare_state_dict(last_state_dict, state_dict)
    if change_result["get_cursor_pos"] == False and state_dict["key_caplock_on"]:  # action
        print("mouse moved", state_dict["get_cursor_pos"])
    if change_result["key_caplock_on"] == False:  # action
        print("CAPSLOCK:", state_dict["key_caplock_on"])
    if change_result["key_scrolllock_on"] == False:  # action
        print("SCROLLLOCK:", state_dict["key_scrolllock_on"])
        if state_dict["key_scrolllock_on"]:
            print("SEND MOUSE DOWN")
        else:
            print("SEND MOUSE UP")
    if change_result["key_numlock_on"] == False:  # action
        print("NUMLOCK:", state_dict["key_numlock_on"])
        if state_dict["key_numlock_on"]:
            print("SEND MOUSE DOWN (Right)")
        else:
            print("SEND MOUSE UP (Right)")

    if change_result["get_read_text_line"] == False:  # action
        print("SEND PASTE:", state_dict["get_read_text_line"])

    pickled = pickle.dumps(local_state_dict)

    # pickle.loads(codecs.decode(pickled.encode(), 'base64')).decode()
    # server.sendto(message, ('<broadcast>', 37020))
    server.sendto(pickled, ('<broadcast>', 37021))

    last_state_dict = state_dict

    time.sleep(0.7)
