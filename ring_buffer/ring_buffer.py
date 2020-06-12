class RingBuffer:
    def __init__(self, capacity):
        self.capacity= capacity
        self.storage = [None for i in range(capacity)]

    def append(self, item):
        #append an item to the end of the buffer list
        # self.storage.append(item)
        # if len(self.storage) == self.capacity:
        #     self.curr = 0
        self.storage.pop(0)
        self.storage[2: 4]
        self.storage.append(item)

    def get(self):
        return self.storage