class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)  # MRU side
        self.tail = Node(-1, -1)  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Move from LRU position
            self.insert(node)  # Move to MRU position
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        if len(self.cache) == self.capacity and self.tail.prev != self.head:
            self.remove(self.tail.prev)  # Remove LRU node

        new_node = Node(key, value)
        self.insert(new_node)

    def remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        del self.cache[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Node):
        """Inserts a node right after the head (MRU side)."""
        self.cache[node.key] = node
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node