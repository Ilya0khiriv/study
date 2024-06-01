import threading
import time


def timer(list):
    for i in list:
        time.sleep(1)
        print(i)


print_ = threading.Thread(target=timer, kwargs=dict(list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print_.start()
timer(list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
print_.join()