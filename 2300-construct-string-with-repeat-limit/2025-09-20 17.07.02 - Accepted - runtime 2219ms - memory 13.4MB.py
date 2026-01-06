class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        counter = Counter(s)
        heap = [(-ord(ch), ch) for ch in counter.keys()]
        heapq.heapify(heap)

        ans = ""
        while heap:
            _, ch = heapq.heappop(heap)

            count = min(counter[ch], repeatLimit)

            # update counter
            counter[ch] -= count
            ans += (ch * count)

            if counter[ch] > 0 and heap:
                _, ch2 = heapq.heappop(heap)
                ans += ch2
                counter[ch2] -= 1

                if counter[ch2] > 0:
                    heapq.heappush(heap, (-ord(ch2), ch2))

                heapq.heappush(heap, (-ord(ch), ch))

        return ans
