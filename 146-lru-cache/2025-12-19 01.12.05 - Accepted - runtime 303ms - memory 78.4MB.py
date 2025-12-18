class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Hashmap to store key-node pairs
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        
        self.head.next = self.tail
        self.tail.prev = self.head

        # needed utils -> add node to linked list (after head)
        #              -> remove node (from anywhere)


    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        # Remove the accessed node from its current position 
        # then move it to the head
        self._remove_node(node)
        self._add_node_after_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add_node_after_head(newNode)
            if len(self.cache) > self.capacity:
                # Pop the tail
                tail = self.tail.prev
                self._remove_node(tail)
                del self.cache[tail.key]
        else:
            # Update the value
            node.value = value
            # Remove the accessed node from its current position 
            # then move it to the head
            self._remove_node(node)
            self._add_node_after_head(node)

    def _add_node_after_head(self, node):
        """Add new node right after the head."""
        prev = self.head
        next = self.head.next

        node.next = next
        node.prev = prev

        prev.next = node
        next.prev = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
