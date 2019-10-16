import ctypes


def get_numlock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x90
    return hllDll.GetKeyState(VK_CAPITAL)


def get_caplock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def get_scrolllock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x91
    return hllDll.GetKeyState(VK_CAPITAL)


if __name__ == '__main__':
    print(get_caplock_state())
    print(get_scrolllock_state())
    print(get_numlock_state())
