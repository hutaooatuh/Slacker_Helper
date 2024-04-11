#remember:pip3 install keyboard
#remember:pip3 install pycaw
from ctypes import windll,cast,POINTER
from keyboard import is_pressed
from time import sleep
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
from json import loads,dump
volume=cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None),POINTER(IAudioEndpointVolume))
hide_list=[]
def write_list():
    global hide_list
    file=open('list.json','w')
    dump(hide_list,file)
    file.close()
def read_list():
    global hide_list
    try:
        file=open('list.json','r')
        hide_list=loads(file.read())
        file.close()
    except:
        write_list()
read_list()
while 1:
    sleep(0.05)
    if hide_list:
        volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0],None)
    if is_pressed('ctrl') and is_pressed('alt') and is_pressed('z'):
        window=windll.user32.GetForegroundWindow()
        windll.user32.ShowWindow(window,0)
        hide_list.append(window)
        write_list()
        volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0],None)
        while is_pressed('ctrl') and is_pressed('alt') and is_pressed('z'):
            sleep(0.05)
    if is_pressed('ctrl') and is_pressed('alt') and is_pressed('s'):
        for i in hide_list:
            windll.user32.ShowWindow(i,1)
        hide_list=[]
        write_list()
        while is_pressed('ctrl') and is_pressed('alt') and is_pressed('s'):
            sleep(0.05)
    if is_pressed('ctrl') and is_pressed('alt') and is_pressed('q'):
        break
