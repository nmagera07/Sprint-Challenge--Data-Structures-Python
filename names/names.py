import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        # >= go right
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value) 
            else: 
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # To search a given key in Binary ¸¸¸¸¸¸¸¸¸compare it with root, if the key is present at root, we return root. If key is greater than root's key, we recur for right subtree of root¸¸¸¸¸¸¸¸¸r left subtree. 
        if self.value == target:
            print(target)
            return True
            
        
        if target < self.value:
            if not self.left:
                return False
            else: 
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BinarySearchTree(names_1[0])
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

