class Queue(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

s = Queue()
print(s.isEmpty())

s.enqueue(6)
s.enqueue(7)
print(s.dequeue())