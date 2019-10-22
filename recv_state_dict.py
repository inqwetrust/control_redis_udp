import pickle
import socket
import traceback
# import pandas as pd
from pandas import DataFrame

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
collected_state_dict = {}
while True:
    try:
        data, addr = client.recvfrom(10240)
        state_dict = pickle.loads(data)
        collected_state_dict[state_dict["get_uuid"]] = state_dict
        collected_state_dict[state_dict["get_server_ip"]] = state_dict
        df = DataFrame(collected_state_dict)
        df.to_html('out.html')
        print("received message:{}".format(state_dict))
    except:
        print(traceback.format_exc())
