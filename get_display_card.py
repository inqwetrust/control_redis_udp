# import os
import subprocess


def get_display_card():
    command = "wmic path win32_VideoController get name "
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ""
    while True:
        line = pipe.stdout.readline()
        if line:
            result += str(line)
        if not line:
            break
    result = result.strip()
    result = result.replace('  ', '')
    result = result.replace('b', '')
    result = result.replace('\\r', '')
    result = result.replace('\\n', '')
    result = result.replace('\'', '')
    result = result.replace('Name', '')
    result = result.strip()
    return result


if __name__ == '__main__':
    print(get_display_card())
