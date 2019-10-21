from ctypes import *

windll = windll.LoadLibrary('user32')
import os
from PIL import Image, ImageDraw, ImageFont
# import datetime
import qrcode

import current_state_dict

dir_path = os.path.dirname(os.path.realpath(__file__))


def set_wallpaper(message):
    drive = "C:\\"
    folder = dir_path
    image = "qr_background.png"

    image_path = os.path.join(drive, folder, image)
    SPI_SETDESKWALLPAPER = 20
    screen_size = windll.GetSystemMetrics(0), windll.GetSystemMetrics(1)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=1,
    )
    img = Image.new('RGB', screen_size, color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    # now = datetime.datetime.now().isoformat()
    d.text((screen_size[0] - 960, 10), '{}'.format(message), fill=(255, 255, 0))
    qr.add_data('{}'.format(message))
    qr.make(fit=True)
    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    pixel_size = qr_code_img.pixel_size
    img.paste(qr_code_img, (screen_size[0] - pixel_size - 150, 50))
    img.save(image_path)
    windll.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    pass


if __name__ == '__main__':
    local_state_dict = current_state_dict.get_current_state_dict()
    print(local_state_dict)
    info_list = []
    info_list.append(local_state_dict["cpu"])
    info_list.append(local_state_dict["ram"])
    info_list.append(local_state_dict["disk"])
    info_list.append(local_state_dict["get_mac_addr"])
    info_list.append(local_state_dict["get_server_ip"])
    info_list.append(local_state_dict["display"])
    info_list.append(local_state_dict["display_card"])
    info_list = ['{}'.format(i) for i in info_list]
    info_list = "|".join(info_list)
    print(info_list)
    set_wallpaper(info_list)
