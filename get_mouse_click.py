# from win32ctypes.pywin32 import win32api
import win32api
import time


def get_left_click():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    return state_left, state_right


if __name__ == '__main__':
    last_state = get_left_click()
    while True:
        state = get_left_click()
        if state != last_state:
            print(get_left_click())
        # time.sleep(1)
        last_state = state
