class Node(object):
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
    def __repr__(self):
        return "data: {}".format(self.data)
n = Node("hi")
n2 = Node("bye", n)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def add(self, data, position=-1):
        if position == -1:
            if self.head == None:
                self.head = Node(data)
            else:
                current_node = self.head
                while current_node.next != None:
                    current_node = current_node.next
                current_node.next = Node(data)
        elif self.length() < position:
            # the postion is outside of the list length?
            return ""
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                if position == 1:
                    new_node = Node(data)
                    new_node.next = current_node.next
                    current_node.next = new_node
                else:
                    current_node = current_node.next 
                position = position - 1
    def remove(self, data):
        if self.head.data == data:
            if self.head.next != None:
                self.head = self.head.next
            else:
                self.head = None
        else:
            current_node = self.head
            while current_node.next != None:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
    def __repr__(self):
        if self.is_empty():
            return "Empty LinkedList"
        current_node = self.head
        while current_node.next != None:
            print(current_node)
            current_node = current_node.next 
        print(current_node)
        return ""
    def is_empty(self):
        return self.head == None
    def length(self):
        if self.is_empty():
            return 0 
        else:
            counter = 1
            current_node = self.head
            while current_node.next != None:
                counter = counter + 1
                current_node = current_node.next 
            return counter
 
 
ll = LinkedList()
ll.add("1")
ll.add("2")
ll.add("3")
ll.add('hi', 2)
ll.add('bye', -1)
print(ll)
 
# print(ll)
# ll.remove("3")
# print(ll)

# ll2 = LinkedList()
# ll2.add('hi')
# ll2.remove('hi')
# print(ll2)
# print("COUNTER:")
# print(ll2.length())

# 🔗 Double Node Implementation
class DoubleNode(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __repr__(self):
        return "data: {}".format(self.data)
    
# 🔗 Double Linked List Implementation
class DoubleLinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def add(self, data, position=-1):
        if position == -1:
            if self.head == None:
                self.head = DoubleNode(data)
            else:
                current_node = self.head
                while current_node.next != None:
                    current_node = current_node.next
                new_node = DoubleNode(data)
                current_node.next = new_node
                new_node.prev = current_node
        elif self.length() < position:
            # the postion is outside of the list length?
            return ""
        elif position == 0:
            new_node = DoubleNode(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                if position == 1:
                    new_node = DoubleNode(data)
                    new_node.next = current_node.next
                    new_node.prev = current_node
                    current_node.next.prev = new_node
                    current_node.next = new_node
                else:
                    current_node = current_node.next 
                position = position - 1