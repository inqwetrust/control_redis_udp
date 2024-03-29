import get_uuid
import get_cursor_pos
import get_local_ip
import get_mac_addr
import get_key_state
import get_read_text_line
import get_mouse_click
import get_cpu_model
import get_ram_info
import get_disk_info
import get_display
import get_display_card
import datetime
import get_mac_csv
import get_pc_remarks

cpu = get_cpu_model.get_cpu_brand()
ram = get_ram_info.get_ram_info()
disk = get_disk_info.get_disk_info()
display = get_display.get_display()
display_card = get_display_card.get_display_card()
start_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
mac_csv = get_mac_csv.get_mac_csv()
pc_remarks = get_pc_remarks.get_pc_remarks_csv()


def get_current_state_dict():
    state_dict = {}
    state_dict["get_uuid"] = get_uuid.get_uuid()
    state_dict["get_cursor_pos"] = get_cursor_pos.queryMousePosition()
    state_dict["get_server_ip"] = get_local_ip.get_local_ip()
    state_dict["get_server_subnet"] = get_local_ip.get_local_subnet()
    state_dict["get_mac_addr"] = get_mac_addr.get_mac_addr()
    if state_dict["get_mac_addr"] in mac_csv:
        state_dict["port_info"] = mac_csv[state_dict["get_mac_addr"]]
    else:
        state_dict["port_info"] = {"room": "room0", "port": 0}
    room_port = '{}_{}'.format(state_dict["port_info"]["room"], state_dict["port_info"]["port"])
    if room_port in pc_remarks:
        state_dict["pc_remarks"] = pc_remarks[room_port]
    else:
        state_dict["pc_remarks"] = {'remarks': '0'}
    click_state = get_mouse_click.get_click_state()
    state_dict["key_caplock_on"] = get_key_state.get_caplock_state() == 1
    state_dict["key_caplock_off"] = get_key_state.get_caplock_state() == 0

    # state_dict["key_scrolllock_on"] = get_key_state.get_scrolllock_state() == 1
    state_dict["key_scrolllock_on"] = click_state[0] == -127 or click_state[0] == -128
    # state_dict["key_scrolllock_off"] = get_key_state.get_scrolllock_state() == 0
    state_dict["key_scrolllock_off"] = click_state[0] == 0 or click_state[0] == 1

    # state_dict["key_numlock_on"] = get_key_state.get_numlock_state() == 1
    state_dict["key_numlock_on"] = click_state[1] == -127 or click_state[1] == -128
    # state_dict["key_numlock_off"] = get_key_state.get_numlock_state() == 0
    state_dict["key_numlock_off"] = click_state[1] == 0 or click_state[1] == 1

    state_dict["get_read_text_line"] = get_read_text_line.get_read_text_line()

    state_dict["cpu"] = cpu
    state_dict["ram"] = ram
    state_dict["disk"] = disk
    state_dict["display"] = get_display.get_display()
    state_dict["display_card"] = display_card
    state_dict["start_time"] = start_time
    state_dict["last_update_time"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return state_dict


def compare_state_dict(last_state_dict, next_state_dict):
    dict_key = [k for k, v in last_state_dict.items()]
    state_change_dict = {}
    for key in dict_key:
        if last_state_dict[key] == next_state_dict[key]:
            state_change_dict[key] = True  # remain same
        else:
            state_change_dict[key] = False  # modified
    return state_change_dict


if __name__ == '__main__':
    import time

    last_state_dict = get_current_state_dict()
    print(last_state_dict)
    print("make change now")
    time.sleep(3)
    next_state_dict = get_current_state_dict()
    print(compare_state_dict(last_state_dict, next_state_dict))
