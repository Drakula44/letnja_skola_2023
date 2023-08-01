import time
position = 0
speed = 3
t = 0.5

while True: 
    s = speed * t
    position += s
    print(position)
    #time.sleep(t)