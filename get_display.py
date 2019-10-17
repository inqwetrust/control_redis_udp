from ctypes import *

windll = windll.LoadLibrary('user32')


def get_display():
    screen_size = windll.GetSystemMetrics(0), windll.GetSystemMetrics(1)
    return screen_size


if __name__ == '__main__':
    print(get_display())
