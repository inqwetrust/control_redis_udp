del *.spec
rmdir /s /q dist
rmdir /s /q build
pyinstaller -F remote_controller.py
pyinstaller -F remote_zombie.py
pyinstaller -F set_wallpaper.py
pyinstaller -F recv_state_dict.py
copy text_list.txt dist\
copy NotoSansTC-Regular.otf dist\
copy room1_mac.csv dist\
copy room2_mac.csv dist\
copy room3_mac.csv dist\
copy room4_mac.csv dist\
copy room5_mac.csv dist\
copy room6_mac.csv dist\
copy pc_remarks.txt dist\
