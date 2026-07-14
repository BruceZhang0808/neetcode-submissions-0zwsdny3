class Node:
    def __init__(self, key: int=0, val: int=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.head.prev = self.head
        self.head.next = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(key, value)
            self.cache[key] = node

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        if len(self.cache) > self.capacity:
            deleted = self.head.prev.key
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
            del self.cache[deleted]
        return
        
