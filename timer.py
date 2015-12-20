import time, pygame
from sys import argv

pygame.init()
pygame.mixer.music.load("/home/mike/func_tools/bicycle_bell.wav")

script_name, wait, unit = argv
wait = float(wait)

if unit == 's':
    sec = wait

elif unit == 'm':
    sec = wait * 60
        
elif unit == 'h':
    sec = wait * 60 * 60

elif unit == 'd':
    sec = wait * 60 * 60 * 24

else:
     print "unit must be 's', 'm', 'h', or 'd'"

time.sleep(sec)
pygame.mixer.music.play()
time.sleep(0.4)

