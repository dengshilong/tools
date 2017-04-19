from blinker import signal

def subscriber(sender):
    print("Got a signal sent by %r" % sender)

ready = signal('ready')
ready.connect(subscriber)

class Processor:
    def __init__(self, name):
        self.name = name

    def go(self):
        ready = signal('ready')
        temp = ready.send(self)
        print(temp)
        print("Processing.")
        complete = signal('complete')
        complete.send(self)

    def __repr__(self):
        return '<Processor %s>' % self.name

temp = ready.send('sdfsdf')
print(temp)
processor_a = Processor('a')
processor_a.go()
