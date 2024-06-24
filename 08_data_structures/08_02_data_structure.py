# Pick one of the abstract data structures mentioned in this section that you have not yet implemented
# Build a custom Python class that demonstrates its functionality 
# Compare your solution to: https://github.com/david-legend/python-algorithms/tree/main/data-structures/src

class BinaryTree:
    # Creation of tree
    
    def __init__(self, size):
        super().__init__()
        self.items = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    #Insert a node into a binary tree
    def insertNode(self, value):
        if self.items is None and (self.lastUsedIndex + 1 == self.maxSize):
            return False
        self.items[self.lastUsedIndex + 1 ] = value
        self.lastUsedIndex += 1
        return True
    
    #Searching a binary tree using levelOrderTraversal
    def search(self, value):
        if (self.items is not None) and (self.lastUsedIndex) > 0:
            for i in range(len(self.items)):
                if self.items[i] == value:
                    return self.items[i]
        return None
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        
        print(self.items[index])
        self.preOrderTraversal(2 * index)
        self.preOrderTraversal((2 * index) + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        
        self.preOrderTraversal(2 * index)
        self.preOrderTraversal((2 * index) + 1)
        print(self.items[index])
        
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return

        self.postOrderTraversal(2 * index)
        self.postOrderTraversal((2 * index) + 1)
        print(self.items[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex):
            print(self.items[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            print("Binary Tree is empty")
            return False
        else:
            for i in range(1, self.lastUsedIndex + 1):
                if self.items[i] == value:
                    self.items[i] == self.items[self.lastUsedIndex]
                    self.items[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    print("Value Deleted")
                    return True
                print("Value was not found")
                return False
    def deleteBinaryTree(self):
        self.items = None
        self.lastUsedIndex = 0
        self.maxSize = 0
        print("Binary Tree Deleted")
        return True
    
newBt = BinaryTree(10)
newBt.insertNode("Drinks")
newBt.insertNode("Hot")
newBt.insertNode("Cold")
newBt.insertNode("Tea")
newBt.insertNode("Coffee")
newBt.insertNode("Beer")
newBt.insertNode("Soda")

print("--- PreOrder Traversal ---")
newBt.preOrderTraversal(1)
print("--- End PreOrder Traversal --- \n\n")

print("--- InOrder Traversal ---")
newBt.inOrderTraversal(1)
print("--- End of InOrder Traversal --- \n\n")

print("--- PostOrder Traversal ---")
newBt.postOrderTraversal(1)
print("--- End of PostOrder Traversal --- \n\n")

print("--- LevelOrder Traversal ---")
newBt.levelOrderTraversal(1)
print("--- End of LevelOrder Traversal --- \n\n")

print("Searching for Coffee, Found --> ",newBt.search("Coffee"))
print("Searching for Scotch, Found --> ",newBt.search("Scotch"), "\n\n")

print("--- Deleting Node with Value 'Cold' ---")
print("Delete Successful? ", newBt.deleteNode("Cold"))
print("--- Printing Values after deletion ---")
newBt.levelOrderTraversal(1)
print("-------- \n\n")