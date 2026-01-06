class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key = lambda e : e[0])

        heap = [(pair[1] - pair[0], pair[0], pair) for pair in events]
        heapq.heapify(heap)

        day = 1
        attended = 0
        rem = []
        while heap:
            _, start, pair = heapq.heappop(heap)
            
            # can we attend
            if pair[0] <= day <= pair[1]:
                print(pair)
                attended += 1
                day = pair[1]
            else:
                rem.append(pair)
                day += 1

        print(rem)
        return attended