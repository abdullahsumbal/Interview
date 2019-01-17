import time

class Cache():

    def __init__(self, size=5):
        self.cacheList = []
        self.cacheKV = {}
        self.Maxsize = size
        self.currSize = 0

    def put(self, item, validTime=2):

        #check if item already exist
        if item in self.cacheKV:
            print("Item {} already in cache".format(item))
            return

        # remove least recently used item.
        if self.currSize == self.Maxsize:
            self.remove()
        # insert at tail if there is space in cache
        self.cacheList.append(item)

        #

        seconds = int(round(time.time()))
        self.cacheKV[item] = [seconds, validTime]
        self.currSize += 1


    def remove(self, index=0):
        del self.cacheKV[self.cacheList[index]]
        self.cacheList.pop(index)


    def print(self):
        print(self.cacheList)
        print(self.cacheKV)

if __name__ == '__main__':
    cache = Cache(5)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    cache.put(3)
    cache.put(5)
    cache.put(6)
    cache.print()
