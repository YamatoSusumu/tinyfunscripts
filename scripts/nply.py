from AppKit import NSSound
from time import sleep
import os.path
from tqdm import tqdm
from sys import stdout

def player_start(sound):

    if not(os.path.isfile(sound)):
        print('Cannot find a sound with filename: ' + sound)
        quit()

    file_name = os.path.basename(sound)[:-4]
    try:
        nssound = NSSound.alloc().initWithContentsOfFile_byReference_(sound, True)
    except:
        print("problem initalizing NSSound with url: " + sound)
        quit()

    nssound.play()

    print('\033[?25l', end="")
    print(">> " + file_name)
    for i in tqdm(range(1, int(nssound.duration())), colour = "#05CDD8", bar_format="  {elapsed} {bar} {remaining}  "):
        sleep(1)

    nssound.stop()
    print('\033[?25h', end="")

path = input("play >> ")

# clear 3 lines
for i in [0,0,0]:
    #cursor up one line
    stdout.write('\x1b[1A')
    #delete last line
    stdout.write('\x1b[2K')

path = path.replace('\\', '').strip()

player_start(path)

