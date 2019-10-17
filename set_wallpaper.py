from ctypes import *

windll = windll.LoadLibrary('user32')
import os
from PIL import Image, ImageDraw, ImageFont
# import datetime
import qrcode

import current_state_dict

def set_wallpaper(message):
    drive = "D:\\"
    folder = "test"
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
    d.text((screen_size[0] - 400, 10), message, fill=(255, 255, 0))
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
    set_wallpaper(local_state_dict)
