import cpuinfo


def get_cpu_brand():
    return cpuinfo.get_cpu_info()["brand"]


if __name__ == '__main__':
    print(get_cpu_brand())
