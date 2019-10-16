import uuid
mac = uuid.getnode()
mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
print(mac)
