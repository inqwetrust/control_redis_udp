import os
import subprocess



def get_disk_info():
    command = "wmic diskdrive get Size"
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ""
    while True:
        line = pipe.stdout.readline()
        if line:
            result += str(line)
        if not line:
            break
    result = [chr if chr.isdigit() else " " for chr in result]
    result = "".join(result)
    result = result.strip()
    result = " ".join(result.split())
    result = result.split()
    result = [float(size) for size in result]
    result = [round(size / 1024 / 1048576, 0) for size in result]
    print(result)
    result = [result.count(ram) for ram in range(1, 128 + 1, 1)]
    return result


if __name__ == '__main__':
    print(get_disk_info())