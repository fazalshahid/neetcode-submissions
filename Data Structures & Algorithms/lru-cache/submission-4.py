class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
    def createNode(self, key, val):
        node = ListNode(key, val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        
        self.head = node
        if not self.tail:
            self.tail = node
        self.cache[key] = node

    def deleteNode(self, key):
        node = self.cache[key]
        if node == self.head:
            self.head = node.next
        if self.tail.key == key:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        del self.cache[key]
        
        
    def get(self, key: int) -> int:
        #print(f"get {key}")
        #print(self.cache)
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.deleteNode(key)
        self.createNode(key, val)
        #print(f"get end {self.cache}")
        #print(f"head {self.head.key} tail {self.tail.key}")
        #print(self.cache[key].val)
        return self.cache[key].val
        
        

    def put(self, key: int, value: int) -> None:
        #print(f"put {key} -> {value}")
        #print(self.cache)
        if key in self.cache:
            self.deleteNode(key)
            self.createNode(key, value)
            return
        if len(self.cache) >= self.capacity:
            self.deleteNode(self.tail.key)
        
        self.createNode(key, value)
        #print(f"put end {self.cache}")
        #print(f"head {self.head.key} tail {self.tail.key}")
