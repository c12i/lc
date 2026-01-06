class MedianFinder(object):
    def __init__(self):
        self.low = []
        self.high = []
    
    def clear(self):
        self.low = []
        self.high = []
    
    def addNum(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        ans = []
        mf = MedianFinder()
        
        for i in range(len(nums) - k + 1):
            mf.clear()
            for j in range(i, i + k):
                mf.addNum(nums[j])
            ans.append(mf.findMedian())
        
        return ans