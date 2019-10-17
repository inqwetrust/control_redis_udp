import os

print(os.system("wmic diskdrive get Name, Manufacturer, Model, InterfaceType, MediaType, SerialNumber, Size"))