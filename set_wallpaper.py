from ctypes import *

windll = windll.LoadLibrary('user32')
import os
from PIL import Image, ImageDraw, ImageFont
# import datetime
import qrcode


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
        box_size=9,
        border=1,
    )
    img = Image.new('RGB', screen_size, color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    # now = datetime.datetime.now().isoformat()
    d.text((1400, 10), message, fill=(255, 255, 0))
    qr.add_data('{}, {}'.format(screen_size, message))
    qr.make(fit=True)
    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    img.paste(qr_code_img, (1200, 50))
    img.save(image_path)
    windll.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    pass


if __name__ == '__main__':
    set_wallpaper("test")
