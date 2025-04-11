import random
import time

def shortpause():
    time.sleep(random.uniform(0.1, 0.5))
def pause():
    time.sleep(random.uniform(0.6, 1))
def longpause():
    time.sleep(random.uniform(1.1, 2))
def thinkhard():
    time.sleep(random.uniform(5, 20))
def wait():
    input("Press the <ENTER> to continue...")