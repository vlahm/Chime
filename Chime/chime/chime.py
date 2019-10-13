#! /home/mike/anaconda3/envs/python3/bin/python

from sys import argv
from time import sleep
from sys import exit
from os.path import realpath
import pyglet, re, subprocess
import threading
import os

path = realpath(__file__)
chimedir = re.match(r'(.*)chime.py', path).group(1)
bell = pyglet.media.load(''.join([chimedir, 'bicycle_bell.wav']))
# bell = pyglet.media.load('/home/mike/git/Chime/Chime/chime/bicycle_bell.wav')
# dur='3s'; reminder='arse'

script_name, dur = argv[0:2]
if len(argv) > 2:
    reminder = argv[2]
else:
    reminder = 'No reminder message'

hms = [None]*3

# parse duration string and convert to seconds
x = re.search(r'[hms]', dur)
if x is None:
    exit("Supply hours, mins, and/or secs in the form 'xhxmxs', where "
    "each 'x' is numeric. No quotes needed.")

hms[0] = re.match(r'((\d+)h)?', dur).group(2)
hms[1] = re.match(r'(?:\d+h)?((\d+)m)?', dur).group(2)
hms[2] = re.match(r'(?:\d+h)?(?:\d+m)?((\d+)s)?', dur).group(2)

hms = [0 if x is None else int(x) for x in hms]

if hms == [0,0,0]:
    exit("Supply hours,w mins, and/or secs in the form 'xhxmxs', where "
    "each 'x' is numeric. No quotes needed.")

def print_message():
    print('Timing for %s hour(s), %s minute(s), and %s second(s).' % tuple(hms))

def timer():
    wait_time = 3600*hms[0] + 60*hms[1] + hms[2]
    sleep(wait_time)

    # open a new terminal window and print reminder
    # 'exec bash' keeps the window open
    # os.system("gnome-terminal -- /bin/bash -c \"echo -e 'Ding!\\n%s\\n'; exec /bin/bash\"" % reminder)
    os.system("notify-send '%s'" % reminder)

    bell.play()
    sleep(0.7)

t1 = threading.Thread(target=timer)
t2 = threading.Thread(target=print_message)
t1.start()
t2.start()
