# Одновязный список:

class Node:
    def init(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def init(self):
        self.head = None

def add(self, data):
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

def reverse(self):
    current_node = self.head
    prev_node = None
    while current_node:
        next_node = current_node.next_node
        current_node.next_node = prev_node
        prev_node = current_node
        current_node = next_node
    self.head = prev_node


# Двусвязный список:

class DNode:
    def init(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None

class DLinkedList:
    def init(self):
        self.head = None
        self.tail = None

def add_first(self, data):
    new_node = DNode(data)
    if not self.head:
        self.head = self.tail = new_node
    else:
        new_node.next_node = self.head
        self.head.prev_node = new_node
        self.head = new_node

def add_last(self, data):
    new_node = DNode(data)
    if not self.tail:
        self.head = self.tail = new_node
    else:
        new_node.prev_node = self.tail
        self.tail.next_node = new_node
        self.tail = new_node

def remove_first(self):
    if not self.head:
        print("List is empty")
        return
    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.head = self.head.next_node
        self.head.prev_node = None

def remove_last(self):
    if not self.tail:
        print("List is empty")
        return
    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.tail = self.tail.prev_node
        self.tail.next_node = None

def reverse(self):
    current_node = self.head
    self.head, self.tail = self.tail, self.head
    while current_node:
        next_node = current_node.next_node
        current_node.next_node = current_node.prev_node
        current_node.prev_node = next_node
        current_node = next_node

def display(self):
    current_node = self.head
    while current_node:
        print(current_node.data, end=" ")
        current_node = current_node.next_node