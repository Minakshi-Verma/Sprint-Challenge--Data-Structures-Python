class RingBuffer:
    def __init__(self, capacity):
        self.capacity= capacity
        self.storage = []
        self.index= 0
    
    def append(self, item):       
        
        # If buffer is not full, it will append the item in the end of the array till it is full
        if len(self.storage)<self.capacity:
            self.storage.append(item)

        #if length of array(buffer) is at full capacity,buffer will replace the item at specific index
        # Ist it will replace the item at index 0
        # after that it will replace the item at index=1 and so on till it reaches to (capacity-1) 
        #For a buffer with capacity=5, index would be 0-4
        # So items will be added at index 0, 1, 2, 3, 4 and then it reaches the capacity and the clock will restart
        else:        
            self.storage[self.index]=item
            #for the array of max capacity=5, index would go to 4 and reset to 0
            if self.index == self.capacity - 1:
                self.index = 0
            else:
                self.index += 1
           
     

    def get(self):      
        return self.storage