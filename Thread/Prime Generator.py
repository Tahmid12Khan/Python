import threading
from queue import Queue
from math import sqrt
#import time
def isPrime(num):
    if num < 2:
        return False
    sqrtNum = sqrt(num)
    sqrtNum += 1
    sqrtNum = int(sqrtNum)

    for i in range(2, sqrtNum):
        if num % i == 0:
            return False

    return True

q = Queue()

def rangePrime(x, y):
    # time.sleep(1)
    #print(threading.current_thread().name, threading.active_count())
    for i in range(x, y + 1):
        if isPrime(i):
            q.put(i)

num = int(input())
sqrtNum = int(sqrt(num))
arr = []

for i in range(1, sqrtNum + 1):
    t = threading.Thread(target=rangePrime, args=((i - 1) * sqrtNum + 1, i * sqrtNum))
    arr.append(t)

if sqrtNum * sqrtNum != num:
    t1 = threading.Thread(target=rangePrime, args=(sqrtNum * sqrtNum, num))
    arr.append(t1)

for t in arr:
    t.start()

for t in arr:
    t.join()

print("Total prime numbers from 1 to {} are {}:".format(num, q.qsize()))
while not q.empty():
    print(q.get())
