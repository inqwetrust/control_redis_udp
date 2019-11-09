import pickle
import socket
import traceback
# import pandas as pd
from pandas import DataFrame
import codecs

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
collected_state_dict = {}
while True:
    try:
        data, addr = client.recvfrom(10240)
        state_dict = pickle.loads(data)
        # collected_state_dict[state_dict["get_uuid"]] = state_dict
        collected_state_dict[state_dict["get_server_ip"]] = state_dict
        collected_state_list = [v for k, v in collected_state_dict.items()]
        df = DataFrame(collected_state_list)
        df = df.drop('get_uuid', 1)
        df = df.drop('get_cursor_pos', 1)
        df = df.drop('get_server_subnet', 1)
        df = df.drop('key_caplock_on', 1)
        df = df.drop('key_caplock_off', 1)
        df = df.drop('key_scrolllock_on', 1)
        df = df.drop('key_scrolllock_off', 1)
        df = df.drop('key_numlock_on', 1)
        df = df.drop('key_numlock_off', 1)
        df = df.drop('get_read_text_line', 1)
        df = df.drop('start_time', 1)
        f = codecs.open('status_report.html', mode='w', encoding='utf-16')
        html = '''<head>
  <meta http-equiv="refresh" content="5">
</head>'''
        html += df.to_html(index=False)
        f.write(html)
        f.close()
        print("received message:{}".format(state_dict))
    except:
        print(traceback.format_exc())
