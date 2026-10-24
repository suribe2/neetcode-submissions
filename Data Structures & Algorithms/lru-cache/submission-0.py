class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None






class LRUCache:

    def __init__(self, capacity: int):
            self.cap = capacity
            self.cache = {} #key -> node

            #Dummy nodes
            self.left = Node(0, 0)
            self.right = Node(0, 0)

            #Link to eachother
            self.left.next = self.right
            self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right
            
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = node.next
        nxt.prev = node.prev

        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
