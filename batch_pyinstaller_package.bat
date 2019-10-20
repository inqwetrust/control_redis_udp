pyinstaller -F remote_controller.py
pyinstaller -F --noconsole --noupx remote_zombie.py
pyinstaller -F --noconsole --noupx set_wallpaper.py
copy text_list.txt dist\
