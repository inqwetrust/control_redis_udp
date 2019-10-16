import pyperclip
import pickle
import socket
import random
import current_state_dict
import pyautogui

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
client2.bind(("", 37021))
last_state_dict = current_state_dict.get_current_state_dict()
local_state_dict = last_state_dict
while True:
    # hash = random.randint(0, 100)

    data, addr = client.recvfrom(10240)
    print("received message:{}".format(data))

    data, addr = client2.recvfrom(10240)
    state_dict = pickle.loads(data)
    change_result = current_state_dict.compare_state_dict(last_state_dict, state_dict)
    if last_state_dict["get_uuid"] == state_dict["get_uuid"]:
        continue
    if local_state_dict["get_server_ip"] == last_state_dict["get_server_ip"] and False:  # ignore checking until deploy
        continue
    if local_state_dict["get_server_subnet"] != state_dict["get_server_subnet"]:
        continue
    if change_result["get_cursor_pos"] == False and state_dict["key_caplock_on"]:  # action
        print("mouse moved", state_dict["get_cursor_pos"])
        pyautogui.moveTo((int(state_dict["get_cursor_pos"]['x']), int(state_dict["get_cursor_pos"]['y'])))
    if change_result["key_caplock_on"] == False:  # action
        print("CAPSLOCK:", state_dict["key_caplock_on"])
    if change_result["key_scrolllock_on"] == False:  # action
        print("SCROLLLOCK:", state_dict["key_scrolllock_on"])
        if state_dict["key_scrolllock_on"]:
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()
    if change_result["key_numlock_on"] == False:  # action
        print("NUMLOCK:", state_dict["key_numlock_on"])
        if state_dict["key_numlock_on"]:
            pyautogui.mouseDown(button='right')
        else:
            pyautogui.mouseUp(button='right')

    if change_result["get_read_text_line"] == False:  # action
        print("TEXT_LINE:", state_dict["get_read_text_line"])
        text_list = state_dict["get_read_text_line"]
        text_list = text_list * 100
        pyperclip.copy(text_list[random.randint(0, 99)])
        pyautogui.hotkey('ctrl', 'v')

    print(change_result)
    last_state_dict = state_dict