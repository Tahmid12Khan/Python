import threading
import time
res = {}

def getMax(arr):
    res['max'] = max(arr)

def getMin(arr):
    res['min'] = min(arr)

def getAvg(arr):
    res['avg'] = sum(arr)/len(arr)

arr = list(map(float, input().split(',')))

thread1 = threading.Thread(target=getMax, args=(arr, ))
thread2 = threading.Thread(target=getMin, args=(arr, ))
thread3 = threading.Thread(target=getAvg, args=(arr, ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print('The average value is: {}'.format(res['avg']))
print('The minimum value is: {}'.format(res['min']))
print('The maximum value is: {}'.format(res['max']))

