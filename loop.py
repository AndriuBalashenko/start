from queue import Queue
from functools import partial

event_loop = None

class EventLoop(Queue):
    def start(self):
        i=0
        while True:
            function = self.get()
            function()
            i-=1
            if i <= 0: break
def buy_water():
    global event_loop
    print("Buy water")
    event_loop.put(buy_water())

def buy_bread():
    global event_loop
    print("Buying bread")
    event_loop.put(buy_water())

event_loop = EventLoop()
event_loop.put(buy_water)
event_loop.start()
