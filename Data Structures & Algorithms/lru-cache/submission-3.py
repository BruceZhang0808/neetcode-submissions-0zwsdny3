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

    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert2head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert2head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

        self.insert2head(node)

        if len(self.cache) > self.capacity:
            deleted = self.head.prev.key
            self.remove(self.head.prev)
            del self.cache[deleted]
        return
        
