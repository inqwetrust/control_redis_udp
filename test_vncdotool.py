from vncdotool import api
client = api.connect('21.127.26.71:5900', password=None)
client.captureScreen('screenshot.png')