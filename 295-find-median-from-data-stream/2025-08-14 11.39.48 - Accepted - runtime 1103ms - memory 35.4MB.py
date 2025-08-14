class MedianFinder(object):

    def __init__(self):
        # max heap for lower half (store negatives)
        self.low = []
        # min heap for upper half
        self.high = []
        

    def addNum(self, num):
        # push into low/ max heap
        heapq.heappush(self.low, -num)

        # ensure order property
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # rebalance sizes so low has same or 1 more element
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))


    def findMedian(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()