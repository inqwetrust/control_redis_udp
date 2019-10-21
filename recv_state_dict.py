import socket
import traceback

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
while True:
    try:
        data, addr = client.recvfrom(10240)
        print("received message:{}".format(data))
    except:
        print(traceback.format_exc())
