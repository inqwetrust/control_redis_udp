pyinstaller -F remote_controller.py
pyinstaller -F --noconsole remote_zombie.py
pyinstaller -F --noconsole set_wallpaper.py
copy text_list.txt dist\
