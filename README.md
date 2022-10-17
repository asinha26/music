# Music

Welcome to my first github commit! This is gonna be a general breakdown of everything in the program and my journey into learning basic multithreading.

I basically started this project because my music app kept having issues with sorting playlists so I started thinking about the code behind it. 
Eventually I opened python and started working on my own music app.

### Music V1
I started experimenting with multiple modules before eventually settling on playsound (not the ideal platform which I corrected later on)
This version only had the play and shuffle buttons. 

### Music V2
In this version I switched to the pygame.mixer module since that would allow more versatility. 
I also created the pause/play and stop buttons

#### Problems
1. The for loop that i used to loop through the songs earlier was now skipping all the songs. 
This didn't happen before because the playsound function stopped the whole program until the sound was done playing. 

2. The pause/play and stop buttons were not able to be clicked because the program was playing the sound

#### Solutions

1. Used a while loop in the if statement that waits until the song is finished playing (mixer.music.getbusy()) or song paused 

2. Discovered ***Multithreading*** and created a new thread that would just play the music so that the main program can manage the buttons

### Music V3
In this version I made some smaller fixes such as removing the for loop for the songs, adding the previous and next track button, and defining the 
thread in the start function so that it can be pressed multiple times. 
I also consolidated everything into functions for readability and efficiency

### Music V4
#### Plans
1. Style the program properly
2. Allow user to import music
