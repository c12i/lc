class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g2 = [-v for v in g]
        heapq.heapify(g2)
        s2 = [-v for v in s]
        heapq.heapify(s2)
        count = 0

        while g2 and s2:
            # O(log n)
            curr_child = -heapq.heappop(g2)            
            curr_cookie = -s2[0]
            # can curr_child be fed?
            if curr_cookie >= curr_child:
                # can be fed, reduce num of cookies
                # O(log m)
                heapq.heappop(s2)
                count += 1

        return count
