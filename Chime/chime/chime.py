from sys import argv
import pyglet, subprocess, time, re, os, sys
from os.path import abspath

bellpath = abspath("/home/mike/func_tools/bicycle_bell.wav")
bell = pyglet.media.load(bellpath)

script_name, dur = argv[0:2]
if len(argv) > 2:
    reminder = argv[2]
else:
    reminder = 'No reminder message'

hms = [None]*3

# parse duration string and convert to seconds
x = re.search(r'[hms]', dur)
if x is None:
    sys.exit("Supply hours, mins, and/or secs in the form 'xhxmxs', where "
    "each 'x' is numeric. No quotes needed.")

hms[0] = re.match(r'((\d+)h)?', dur).group(2)
hms[1] = re.match(r'(?:\d+h)?((\d+)m)?', dur).group(2)
hms[2] = re.match(r'(?:\d+h)?(?:\d+m)?((\d+)s)?', dur).group(2)

hms = [0 if x is None else int(x) for x in hms]

if hms == [0,0,0]:
    sys.exit("Supply hours,w mins, and/or secs in the form 'xhxmxs', where "
    "each 'x' is numeric. No quotes needed.")

print('Timing for %s hour(s), %s minute(s), and %s second(s).' % tuple(hms))

wait_time = 3600*hms[0] + 60*hms[1] + hms[2]
time.sleep(wait_time)

# open a new terminal window and print reminder 
# 'exec bash' keeps the window open
gnome_command = "bash -c \"echo -e 'Ding!\\n%s'; exec bash\"" % reminder
subprocess.call(['gnome-terminal', '-e', gnome_command])

# remove dumpfile
dumpfile = abspath("/home/mike/git/funcs/Chime/chime/nohup.out")
#try:
#    os.remove(dumpfile)
#except OSError:
#    pass

bell.play()
time.sleep(0.7)

