import traceback

import pyperclip
import pickle
import socket
import random
import current_state_dict
import pyautogui

pyautogui.FAILSAFE = False

client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

client2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client2.bind(("", 37021))
last_state_dict = current_state_dict.get_current_state_dict()
local_state_dict = last_state_dict
print(local_state_dict)

# send back config
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.01)
server.bind(("", 44443))
pickled = pickle.dumps(local_state_dict)
server.sendto(pickled, ('<broadcast>', 37020))
udp_recv_count = 0
while True:
    # hash = random.randint(0, 100)
    try:
        udp_recv_count += 1
        if udp_recv_count % 250 == 0:
            last_state_dict = current_state_dict.get_current_state_dict()
            pickled = pickle.dumps(last_state_dict)
            server.sendto(pickled, ('<broadcast>', 37020))
        data, addr = client2.recvfrom(10240)
        state_dict = pickle.loads(data)
        change_result = current_state_dict.compare_state_dict(last_state_dict, state_dict)
        if last_state_dict["get_uuid"] == state_dict["get_uuid"]:
            continue
        if local_state_dict["get_server_ip"] == last_state_dict["get_server_ip"] and False:  # False = ignore checking
            continue
        if local_state_dict["get_server_subnet"] != state_dict["get_server_subnet"]:
            continue
        if change_result["get_cursor_pos"] == False and state_dict["key_caplock_on"]:  # action
            print("mouse moved", state_dict["get_cursor_pos"])
            pyautogui.moveTo((int(state_dict["get_cursor_pos"]['x']), int(state_dict["get_cursor_pos"]['y'])))
        if change_result["key_caplock_on"] == False:  # action
            print("CAPSLOCK:", state_dict["key_caplock_on"])
        if change_result["key_scrolllock_on"] == False and state_dict["key_caplock_on"]:  # action
            print("Left Click:", state_dict["key_scrolllock_on"])
            if state_dict["key_scrolllock_on"]:
                pyautogui.mouseDown()
                print("RECV: MOUSE DOWN")
            elif state_dict["key_scrolllock_off"]:
                pyautogui.mouseUp()
                print("RECV: MOUSE UP")
        if change_result["key_numlock_on"] == False and state_dict["key_caplock_on"]:  # action
            print("Right Click:", state_dict["key_numlock_on"])
            if state_dict["key_numlock_on"]:
                pyautogui.mouseDown(button='right')
                print("RECV: MOUSE DOWN (right)")
            elif state_dict["key_numlock_off"]:
                pyautogui.mouseUp(button='right')
                print("RECV: MOUSE UP (right)")

        if change_result["get_read_text_line"] == False:  # action
            print("TEXT_LINE:", state_dict["get_read_text_line"])
            text_list = state_dict["get_read_text_line"]
            text_list = text_list * 100
            pyperclip.copy(text_list[random.randint(0, 99)])
            pyautogui.hotkey('ctrl', 'v')

        # print(change_result)
        last_state_dict = state_dict
    except:
        print(traceback.format_exc())
