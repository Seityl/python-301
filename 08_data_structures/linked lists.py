# Build a custom `Stack` similar to the `Queue` you built

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def __repr__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            prevNode = self.getNode(index - 1)
            newNode.next = prevNode.next
            prevNode.next = newNode
        self.length += 1
    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head - self.head.next
        else:
            prevNode = self.getNode(index - 1)
            prevNode.next = prevNode.next.next
        self.length -= 1    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print(ll)

ll.prepend(5)
print(ll)

node = ll.getNode(1)
print(node.value)

print(node)

ll.remove(2)
print(ll)
ll.insert(3, 100)
print(ll)