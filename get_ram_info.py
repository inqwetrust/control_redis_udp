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
    result = [str(result[r]) + "x" + "{}".format(r + 1) for r in range(0, 32 + 0, 1)]
    result = [r if r[0] != '0' else None for r in result]
    result = list(filter(None, result))
    return result


if __name__ == '__main__':
    print(get_ram_info())
