import time
import random
from queue import Queue
from threading import Lock, Thread

class Cache():

    def __init__(self, size=5):
        self.cacheList = []
        #self.cacheList = Queue()
        self.cacheKV = {}
        self.Maxsize = size
        self.currSize = 0
        self.queueLock = Lock()

    def put(self, item, validTime=2):
        #check if item already exist
        if item in self.cacheKV:
            #check if it has expired
            insertTime, duration = self.cacheKV[item]
            seconds = int(round(time.time()))
            if insertTime + duration > seconds:
                print("Item {} already in cache".format(item))
                return
            else:
                print("Item {} expired".format(item))
                self.remove(self.cacheList.index(item))

        # remove least recently used item.
        if self.currSize == self.Maxsize:
            self.remove()

        self.add(item, validTime)


    def add(self, item, validTime):
        self.queueLock.acquire()
        try:
            # insert at tail if there is space in cache
            self.cacheList.append(item)
            seconds = int(round(time.time()))
            self.cacheKV[item] = [seconds, validTime]
            self.currSize += 1
            print("Item {} added in cache".format(item))
        finally:
            self.queueLock.release() #release lock

    def remove(self, index=0):
        self.queueLock.acquire()
        try:
            item = self.cacheList.pop(index)
            del self.cacheKV[item]
            self.currSize -= 1
            print("Item {} removed from cache".format(item))
        finally:
            self.queueLock.release() #release lock



    def print(self):
        print(self.cacheList)
        print(self.cacheKV)


def traffic(cache):
    # create traffic
    while True:
        item = random.randint(1,10)
        validTime = random.randint(1,10)
        cache.put(item, validTime)
        cache.print()
        time.sleep(5)


if __name__ == '__main__':

    # initize Cache with size
    cache = Cache(5)

    # thread pool
    threads = []
    for i in range(2):
         t = Thread(target=traffic, args=(cache,))
         threads.append(t)

    # start threads
    for thread in threads:
        thread.start()
    # wait until all threads are executed
    for thread in threads:
         thread.join()
