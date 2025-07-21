import heapq

class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.timestamp = 0  # updated explicitly from LFUCache
        self.valid = True   # used to mark stale nodes

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.timestamp < other.timestamp
        return self.freq < other.freq

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}    # key -> node
        self.heap = []
        self.timestamp = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node, node.value)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            self._update(node, value)
        else:
            if len(self.cache) >= self.capacity:
                self._evict()
            new_node = Node(key, value)
            new_node.timestamp = self.timestamp
            self.timestamp += 1
            self.cache[key] = new_node
            heapq.heappush(self.heap, new_node)

    def _update(self, node, value):
        node.valid = False  # mark old node as stale
        new_node = Node(node.key, value, node.freq + 1)
        new_node.timestamp = self.timestamp
        self.timestamp += 1
        self.cache[node.key] = new_node
        heapq.heappush(self.heap, new_node)

    def _evict(self):
        while self.heap:
            node = heapq.heappop(self.heap)
            if node.valid:
                del self.cache[node.key]
                break
