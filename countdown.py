# countdown.py - simple timer countdown

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# play a sound at the end
subprocess.Popen(['open','alarm.wav'])

