# Build a custom `Stack` similar to the `Queue` you built
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.height = 0

    # Checks whether there are any elements in the stack
    def isEmpty(self):
        return self.height == 0

    # Adds an element to the collection
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.bottom = newNode
        self.top = newNode
        self.height += 1

    # Removes the most recently added element from the collection
    def pop(self):
        if self.isEmpty():
            return None
        else:
            popNode = self.top
            self.top = self.top.next
            self.height -= 1
            if self.isEmpty():
                self.bottom = None
            return popNode.value
    # Returns the topmost element without removing it from the stack    
    def peek(self):
        return self.top.value

    # Returns the total size of the stack
    def checkSize(self):
        return self.height
    
    def __repr__(self):
        node = self.top
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

sandwich = Stack()

sandwich.push("Bottom Bread")
sandwich.push("Mayo")
sandwich.push("Lettuce")
sandwich.push("Egg")
sandwich.push("Top Bread")

print(sandwich)

sandwich.pop()
print(sandwich)

print(sandwich.checkSize())
print(sandwich.peek())