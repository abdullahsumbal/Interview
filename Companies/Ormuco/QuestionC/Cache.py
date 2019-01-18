import time
import random
from threading import Lock, Thread

class Cache():
    """
    This is implements the least recently used cache with time expiry
    """

    def __init__(self, size=5):
        self.cacheList = []
        self.cacheKV = {}
        self.Maxsize = size
        self.currSize = 0

    def put(self, item, validTime=2):
        """
        This method is responsible for removing items before adding into the queue. It also removes the item if it is expired
        """
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
        if len(self.cacheKV) >= self.Maxsize:#self.currSize == self.Maxsize:
            self.remove()

        # add item to list/queue
        self.add(item, validTime)


    def add(self, item, validTime):
        """
        Add item into the list and update the (key,value) map
        """
        self.cacheList.append(item)
        seconds = int(round(time.time()))
        self.cacheKV[item] = [seconds, validTime]
        print("Item {} added in cache".format(item))

    def removeItem(self, item):
        """
        Remove desired item form the queue. Also remove item from map.
        """
        index = self.cacheList.index(item)
        self.cacheList.pop(index)
        del self.cacheKV[item]
        print("Item {} removed from cache".format(item))

    def remove(self, index=0):
        """
        Remove item at desired index form the queue( or start of the list by default). Also update map
        """
        item = self.cacheList.pop(index)
        del self.cacheKV[item]
        print("Item {} removed from cache".format(item))


    def print(self):
        """
        For printing queue and Map
        """
        print("Items in the Cache")
        print("Items", self.cacheList)
        print("Key Value of items: ", self.cacheKV)

lock = Lock()
def traffic(cache):

    # create traffic
    while True:
        # create random item and valid times
        item = random.randint(1,9)
        validTime = random.randint(1,3)
        lock.acquire()
        try:
            cache.put(item, validTime)
            cache.print()
        finally:
            lock.release()
        # delay to obersve the output
        time.sleep(1)


if __name__ == '__main__':

    sources = 1
    cacheSize = 5
    # initize Cache with size
    cache = Cache(cacheSize)

    # thread pool
    threads = []
    for i in range(sources):
         t = Thread(target=traffic, args=(cache,))
         threads.append(t)

    # start threads
    for thread in threads:
        thread.start()
    # wait until all threads are executed
    for thread in threads:
         thread.join()
