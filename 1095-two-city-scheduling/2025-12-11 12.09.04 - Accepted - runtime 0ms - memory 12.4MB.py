class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        A, B = [], []
        costA = costB = 0

        for i in range(len(costs)):
            a, b = costs[i]
            if a <= b:
                heapq.heappush(A, ((b - a), a, b))
                costA += a
            else:
                heapq.heappush(B, ((a - b), a, b))
                costB += b

        target = n // 2

        while len(A) > target:
            _, ca, cb = heapq.heappop(A)
            costA -= ca
            costB += cb

        while len(B) > target:
            _, ca, cb = heapq.heappop(B)
            costB -= cb
            costA += ca
            
        return costA + costB
