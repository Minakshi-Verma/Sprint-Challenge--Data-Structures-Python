import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
     
        #if node is instantiated with None or node has no value
        if self.value is None:
            #set self.value to the value of inserted node
            self.value = value
        # if node already has a value(self.value) and inserted value >= existing node value
        elif value >= self.value:
            # if new value is greater...it will go on right, check if we already have a node on right
            if self.right:
            # if node.right is there, insert the value
                self.right.insert(value)            
            # if there is no right node, insert the new node with the value
            else:
                self.right = BSTNode(value)
        #Now if the value< self.value, we insert the new value on left(check using ifel or just move to else block)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)  
    #-------------------------------------     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value ==target:
            return True

        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)

        elif self.value< target:
            if self.right:
                return self.right.contains(target)
        else:
            return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#Took 13.81200 sec with double nested loop

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:    
#             duplicates.append(name_1)

#Using BST tree
#Create a BST tree of name_1 list using insert method
# self.bst.insert(node)
new_tree = BSTNode('tree')

for name in names_1:
    new_tree.insert(name)

for name in names_2:
    if new_tree.contains(name):
        duplicates.append(name) 

#run time is now 0.22 second ( from 13+ seconds using nested loop)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
