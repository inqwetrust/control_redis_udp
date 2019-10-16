import pyautogui
import pyperclip


def text_copy():
    pyperclip.copy("abc")


def test_paste():
    pyautogui.hotkey('ctrl', 'v')
