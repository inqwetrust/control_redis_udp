# import os
import subprocess


def get_ram_info():
    command = "wmic memorychip get /VALUE |findstr \"Capacity\""
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ""
    while True:
        line = pipe.stdout.readline()
        if line:
            result += str(line)
        if not line:
            break
    result = [result.count("{}".format(ram * 1024 * 1048576)) for ram in range(1, 32 + 1, 1)]
    return result


if __name__ == '__main__':
    print(get_ram_info())
