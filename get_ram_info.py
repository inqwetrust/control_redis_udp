import os
from ctypes import *
from ctypes.wintypes import *


class MEMORYSTATUS(Structure):
    _fields_ = [
        ('dwLength', DWORD),
        ('dwMemoryLoad', DWORD),
        ('dwTotalPhys', DWORD),
        ('dwAvailPhys', DWORD),
        ('dwTotalPageFile', DWORD),
        ('dwAvailPageFile', DWORD),
        ('dwTotalVirtual', DWORD),
        ('dwAvailVirtual', DWORD),
    ]


def winmem():
    x = MEMORYSTATUS()
    windll.kernel32.GlobalMemoryStatus(byref(x))
    return x


if __name__ == '__main__':
    print(winmem().dwTotalPhys)
    print(os.system("wmic memorychip get /VALUE |findstr \"Capacity\""))
