from time import strftime
import psutil as ps
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
import random

x1 = []
y1 = []
time = 0
fig = plt.figure()

def animate(i):
    x = ps.cpu_percent()
    t = strftime('%Y-%m-%d %H:%M:%S')
    x1.append(t)
    y1.append(x)

    if len(x1) > 15:
        x1.pop(0)
        y1.pop(0)

    dates = [dateutil.parser.parse(s) for s in x1]
    ax1 = plt.gca()
    ax1.clear()
    ax1.set_xticks(dates)
    xfmt = md.DateFormatter('%H:%M:%S')
    ax1.xaxis.set_major_formatter(xfmt)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)
    plt.xlabel("time (h:m:s)")
    plt.ylabel("CPU usage")
    num = random.randint(0, 4)
    col = ['r', 'b', 'c', 'k', 'g']
    ax1.plot(dates, y1, "o-", color =col[num])

ani = animation.FuncAnimation(fig, animate, interval = 2000)
plt.show()
