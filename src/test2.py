import time
import throttle

t = throttle.Throttle(26)

while True:
    percent:float = t.read()
    print(percent)
    time.sleep(0.25)