del *.spec
pyinstaller -F remote_controller.py
pyinstaller -F remote_zombie.py
pyinstaller -F set_wallpaper.py
pyinstaller -F recv_state_dict.py
copy text_list.txt dist\
