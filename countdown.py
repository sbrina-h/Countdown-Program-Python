
import time, subprocess

timer = 10

while timer > 0:
    print(timer)

    time.sleep(1)

    timer -= 1

subprocess.Popen(['open', 'alarm.wav'])
