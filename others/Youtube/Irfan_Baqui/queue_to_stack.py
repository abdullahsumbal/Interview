"""
1. Use two stack as a queue.
2. Use a stack as a queue.
"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Queue1:
    def __init__(self):
        self.enqueueStack = Stack()
        self.dequeueStack = Stack()


    def Dequeue(self):
        # dequeue there

        # check if the dequeueStack is isEmpty then transfer item from the enqueueStack
        if(self.dequeueStack.size() == 0):
            if (self.enqueueStack.size() == 0):
                print(" the queue is empty")
                return
            else: # transfer all the item from the EnqueueStack to DequeueStack
                while(self.enqueueStack.size() != 0):
                    self.dequeueStack.push(self.enqueueStack.pop())
        result = self.dequeueStack.pop()
        print(result)


    def Enqueue(self, val):
        # enqueue
        self.enqueueStack.push(val)

class Queue2:
    def __init__(self):
        self.stack = Stack()


    def Dequeue(self):
        if(self.stack.size() == 0):
            print("The queue is empty")
        else:
            print(self.rec())

    def rec(self):
        if(self.stack.size() == 1):
            return self.stack.pop()
        val = self.stack.pop()
        result = self.rec()
        self.stack.push(val)
        return result


    def Enqueue(self, val):
        # enqueue
        self.stack.push(val)


if __name__ == "__main__":
    queue = Queue2()
    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Dequeue()
    queue.Dequeue()
    queue.Enqueue(4)
    queue.Enqueue(5)
    queue.Dequeue()
    queue.Dequeue()
