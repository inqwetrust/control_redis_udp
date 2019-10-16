import get_uuid
import get_cursor_pos
import get_local_ip
import get_mac_addr
import get_key_state
import get_read_text_line


def get_current_state_dict():
    state_dict = {}
    state_dict["get_uuid"] = get_uuid.get_uuid()
    state_dict["get_cursor_pos"] = get_cursor_pos.queryMousePosition()
    state_dict["get_server_ip"] = get_local_ip.get_local_ip()
    state_dict["get_server_subnet"] = get_local_ip.get_local_subnet()
    state_dict["get_mac_addr"] = get_mac_addr.get_mac_addr()
    state_dict["key_caplock_on"] = get_key_state.get_caplock_state() == 1
    state_dict["key_caplock_off"] = get_key_state.get_caplock_state() == 0
    state_dict["key_scrolllock_on"] = get_key_state.get_scrolllock_state() == 1
    state_dict["key_scrolllock_off"] = get_key_state.get_scrolllock_state() == 0
    state_dict["key_numlock_on"] = get_key_state.get_numlock_state() == 1
    state_dict["key_numlock_off"] = get_key_state.get_numlock_state() == 0
    state_dict["get_read_text_line"] = get_read_text_line.get_read_text_line()
    return state_dict


def compare_state_dict(last_state_dict, next_state_dict):
    dict_key = [k for k, v in last_state_dict.items()]
    state_change_dict = {}
    for key in dict_key:
        if last_state_dict[key] == next_state_dict[key]:
            state_change_dict[key] = True
        else:
            state_change_dict[key] = False
    return state_change_dict


if __name__ == '__main__':
    import time
    last_state_dict = get_current_state_dict()
    print("make change now")
    time.sleep(3)
    next_state_dict = get_current_state_dict()
    print(compare_state_dict(last_state_dict, next_state_dict))
