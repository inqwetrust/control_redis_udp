import tableprint as tp
from pandas import DataFrame
import get_uuid

while True:
    lol = [[get_uuid.get_uuid()[:5] for r in range(5)] for rr in range(5)]
    headers = [get_uuid.get_uuid()[:5] for r in range(5)]
    data = DataFrame(lol, columns=headers)
    tp.dataframe(data)
