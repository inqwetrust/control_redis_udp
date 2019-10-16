import pyautogui
import pyperclip


def text_copy():
    pyperclip.copy("abc")


def text_paste():
    pyautogui.hotkey('ctrl', 'v')


if __name__ == '__main__':
    text_copy()
    text_paste()
