import heapq

class AllOne(object):
    def __init__(self):
        self.store = {}

        self._min_heap = []
        self._max_heap = []


    def inc(self, key):
        if key in self.store:
            new_count = self.store[key] + 1
        else:
            new_count = 1

        self.store[key] = new_count
        heapq.heappush(self._min_heap, (new_count, key))
        heapq.heappush(self._max_heap, (-new_count, key))


    def dec(self, key):
        if key not in self.store:
            return

        curr = self.store[key]
        if curr == 1:
            # remove the key entirely
            del self.store[key]
        else:
            new_count = curr - 1
            self.store[key] = new_count
            heapq.heappush(self._min_heap, (new_count, key))
            heapq.heappush(self._max_heap, (-new_count, key))


    def getMaxKey(self):
        self._clean_max()
        if not self._max_heap:
            return ""
        return self._max_heap[0][1]


    def getMinKey(self):
        self._clean_min()
        if not self._min_heap:
            return ""
        return self._min_heap[0][1]


    def _clean_min(self):
        while self._min_heap:
            cnt, key = self._min_heap[0]
            if key not in self.store or self.store[key] != cnt:
                heapq.heappop(self._min_heap)
            else:
                break

    def _clean_max(self):
        while self._max_heap:
            negcnt, key = self._max_heap[0]
            cnt = -negcnt
            if key not in self.store or self.store[key] != cnt:
                heapq.heappop(self._max_heap)
            else:
                break
