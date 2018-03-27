import threading
import random
import time

t = threading.Lock()

def isInsideCircle(x, y):
    return x * x + y * y <= 1.0

count = 0
total = 0

def randomGenerator():
    global count
    global total
    time.sleep(0.1)
    #print(threading.current_thread().name, threading.active_count())
    for i in range(100000):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        with t:
            if isInsideCircle(x, y):
                count += 1
            total += 1

#tt = time.time()
arr = []

for i in range(10):
    t1 = threading.Thread(target=randomGenerator)
    arr.append(t1)
    t1.start()

for thread in arr:
    thread.join()

print('Total points inside the square = {}.\n'
      'Total points in the circle = {}.\n'
      'Value of the pi from calculation = {}.'
      .format(total, count, (4 * count)/total))
