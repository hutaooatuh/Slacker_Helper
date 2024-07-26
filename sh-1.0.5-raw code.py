from ctypes import windll
from keyboard import is_pressed
from time import sleep
hide_list=[]
while 1:
    sleep(0.08)
    if is_pressed('ctrl') and is_pressed('alt') and is_pressed('z'):
        window=windll.user32.GetForegroundWindow()
        windll.user32.ShowWindow(window,0)
        hide_list.append(window)
        while is_pressed('ctrl') and is_pressed('alt') and is_pressed('z'):
            sleep(0.08)
    if is_pressed('ctrl') and is_pressed('alt') and is_pressed('s'):
        if hide_list:
            windll.user32.ShowWindow(hide_list[-1],1)
            hide_list.pop()
        while is_pressed('ctrl') and is_pressed('alt') and is_pressed('s'):
            sleep(0.08)
