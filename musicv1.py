#Prolog
# Aaryak Sinha
# aaryaksinha@gmail.com

r"""
Purpose:
Make a music program that can pause/play, next track, prev. track, and shuffle 
"""

from playsound import playsound
from tkinter import *
from tkinter import ttk
import random
from time import *

upcoming = {
    'Song 1, 6 seconds' : 'audio_files/sample-6s.mp3',
    'Song 2, 9 seconds' : 'audio_files/sample-9s.mp3',
    'Song 3, 12 seconds' : 'audio_files/sample-12s.mp3' 
}

keys = list(upcoming.keys())
currentSong = None
upnextlist = None

def start():
    print('start pressed')
    play()

def shuffle():
    print('shuffle pressed')
    random.shuffle(keys)
    play()

# For future implementation
'''
def playPause():
    print('playpause pressed')

def nextTrack():
    print('next pressed')

def prevTrack():
    print('prev pressed')

def stop():
    print('stop pressed')
'''

def play():
    
    upnextlist = ''
    for j in keys:
        upnextlist += str(j + '\n')
    for i in keys:
        currentSong = i
        current.config(text="Current song:{}".format(currentSong))
        upnextlist = upnextlist.replace(i, '')
        upnextlist = upnextlist[1:]
        upnext.config(text='Up next:\n{}'.format(upnextlist))
        window.update()
        playsound(upcoming[i])


window = Tk()
window.title("Aaryak's Music App")
window.geometry('600x600')

frm = ttk.Frame(window, padding=10)
frm.grid()

current = Label(frm, text="Current song:{}".format(currentSong), font=('consolas',20))
current.grid(column=1, row=0)

upnext = Label(frm, text='Up next:\n{}'.format(upnextlist), font=('consolas',20))
upnext.grid(column=1, row=3)

startButton = ttk.Button(frm, text="start", command=start).grid(column=0, row=1)
shuffleButton = ttk.Button(frm, text="shuffle", command=shuffle).grid(column=2, row=1)

'''
playpauseButton = ttk.Button(frm, text="play/pause", command=playPause).grid(column=1, row=1)
nexttrackButton = ttk.Button(frm, text="next", command=nextTrack).grid(column=2, row=2)
prevtrackButton = ttk.Button(frm, text="prev", command=prevTrack).grid(column=0, row=2)
stopButton = ttk.Button(frm, text="stop", command=stop).grid(column=1, row=2)
'''

window.mainloop()

#FIXME
# 1. Fix the grid so it stays still
#   https://stackoverflow.com/questions/10826738/setting-uneven-cell-heights-in-a-tkinter-gui-using-grid
# 2. Make songs stoppable 


#TODO
# 1. All other buttons (next, prev, stop, pause)
# 2. User imports music

#Notes
'''
May have to use something other than playsound module so that songs will stop
'''

# Button styling
    #Button option 1
    # test = Button(frm, text="Test", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=start).grid(column=0, row=2)

    #Button option 2
    # https://stackoverflow.com/questions/39054156/tkinter-custom-create-buttons