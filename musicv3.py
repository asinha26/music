#Prolog
# Aaryak Sinha
# aaryaksinha@gmail.com

r"""
Purpose:
Make a music program that can pause/play, next track, prev. track, and shuffle 
"""

from tkinter import *
from tkinter import ttk
from pygame import mixer, time
import random
import threading
#from tkinter import filedialog (for later)
#import os (for later)

# Makes a playlist 
#   (will change later so that user can input their own music)
upcoming = {
    'Song 1, 6 seconds' : 'audio_files/sample-6s.mp3',
    'Song 2, 9 seconds' : 'audio_files/sample-9s.mp3',
    'Song 3, 12 seconds' : 'audio_files/sample-12s.mp3' 
}

# Gets keys of the playlist
keys = list(upcoming.keys())

#Initializes all of the global variables 
#   (in a function so that we can reset program easily)
def resetVars():
    global currentSong, upnextlist, nextCheck, stopped, pausecheck, prevCheck, i, prev
    currentSong = None
    upnextlist = None
    pausecheck = 0
    nextCheck = False
    prevCheck = False
    i = 0
    stopped = False
    prev = False

#Start button function
def start():
    resetVars()
    
    #creates a new thread so that other functions will work while music is playing
    t2 = threading.Thread(target=play, args=(keys))
    t2.start()

#shuffle button function
def shuffle():
    resetVars()
    shuf_keys = keys
    random.shuffle(shuf_keys)
    
    #creates a new thread so that other functions will work while music is playing
    t2 = threading.Thread(target=play, args=(shuf_keys))
    t2.start()

#pause/play button function
def playPause():
    global pausecheck
    pausecheck += 1
    # if pause has already been clicked then it will pause, otherwise it will resume
    if pausecheck%2 == 1:
        mixer.music.pause()
    else:
        mixer.music.unpause()

#next track button function
def nextTrack():
    global nextCheck
    nextCheck = True
        
#previous track button function
def prevTrack():
    global prevCheck
    prevCheck = True

#updates all the labels in the window 
def windowConfig():
    global currentSong, upnextlist
    current.config(text="Current song:{}".format(currentSong))
    upnext.config(text='Up next:\n{}'.format(upnextlist))
    window.update()

#stop button function
def stop():
    global stopped
    resetVars()
    mixer.music.stop()
    stopped = True
    global currentSong, upnextlist
    currentSong = None
    upnextlist = None
    windowConfig()

#plays the music 
def play(*keys):
    global upnextlist, nextCheck, pausecheck, currentSong, i, prevCheck, prev
    i = 0
    upnextlist = ''
    
    #Creates a "list" (string) for upcoming songs
    for j in keys:
        upnextlist += str(j + '\n')
    
    #Loop for the music 
    while i < len(keys):
        currentSong = keys[i]
        
        #updates the upcoming songs list
        if not(prev):
            upnextlist = upnextlist.replace(keys[i], '')
            upnextlist = upnextlist[1:]
            prev = False
        windowConfig()
        mixer.music.load(upcoming[keys[i]])
        mixer.music.play()
        
        #next song will not play until previous song is finished
        clock = time.Clock()
        clock.tick(10)
        while mixer.music.get_busy() or pausecheck%2 == 1:
            clock.tick(10)
            if nextCheck == True:
                nextCheck = False
                break
            if prevCheck == True and i > 0:
                prevCheck = False
                i-=2
                break
            elif prevCheck == True and i == 0:
                prevCheck = False
                prev = True
                mixer.music.rewind()
        if stopped:
            break
        i+=1

resetVars()

#creates initial window
window = Tk()
window.title("Aaryak's Music App")
window.geometry('600x600')

mixer.init()

frm = ttk.Frame(window, padding=10)
frm.grid()

current = Label(frm, text="Current song:{}".format(currentSong), font=('consolas',20))
current.grid(column=1, row=0)

upnext = Label(frm, text='Up next:\n{}'.format(upnextlist), font=('consolas',20))
upnext.grid(column=1, row=3)

startButton = ttk.Button(frm, text="start", command=start).grid(column=0, row=1)
shuffleButton = ttk.Button(frm, text="shuffle", command=shuffle).grid(column=2, row=1)
playpauseButton = ttk.Button(frm, text="play/pause", command=playPause).grid(column=1, row=1)

nexttrackButton = ttk.Button(frm, text="next", command=nextTrack).grid(column=2, row=2)

prevtrackButton = ttk.Button(frm, text="prev", command=prevTrack).grid(column=0, row=2)

stopButton = ttk.Button(frm, text="stop", command=stop).grid(column=1, row=2)

window.mainloop()

#FIXME
# 1. Fix the grid so it stays still
#   https://stackoverflow.com/questions/10826738/setting-uneven-cell-heights-in-a-tkinter-gui-using-grid
# (done) 2. Make songs stoppable 


#TODO
# (done) 1. All other buttons (next, prev, stop, pause)
# 2. User imports music

# Button styling
    #Button option 1
    # test = Button(frm, text="Test", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=start).grid(column=0, row=2)

    #Button option 2
    # https://stackoverflow.com/questions/39054156/tkinter-custom-create-buttons