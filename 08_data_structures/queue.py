class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def isEmpty(self):
        return self.head is None
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.value
    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            dequeuedNode = self.head
            self.head = self.head.next
            self.length -= 1
            if self.isEmpty():
                self.tail = None
            return dequeuedNode.value
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
morningTasks = Queue()

morningTasks.enqueue("Wake Up")
morningTasks.enqueue("Work Out")
morningTasks.enqueue("Go To Work")

morningTasks.peek()

task =  morningTasks.dequeue()

print(f"TODO: {task}")
print(morningTasks)