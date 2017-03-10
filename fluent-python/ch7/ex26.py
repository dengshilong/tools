import time
from clockdeco_param import clock


@clock()
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)


@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(.123)
