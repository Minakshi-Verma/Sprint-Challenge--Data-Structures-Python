class RingBuffer:
    def __init__(self, capacity):
        self.capacity= capacity
        self.storage = []

    def append(self, item):            
        # append the new item
        self.storage.append(item)
        self.storage.pop(0)
        self.storage.append(item)
        # del self.storage[5:5]       
        
        # del self.storage[0:1]

    def get(self):
        return self.storage