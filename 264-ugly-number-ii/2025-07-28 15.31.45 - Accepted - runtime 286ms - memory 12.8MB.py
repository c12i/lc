class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        seen = set([1])
        curr = None

        for _ in range(n):
            curr = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                nxt = curr * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return curr
