class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        prev_end = float("-inf")
        overlaps = 0

        intervals.sort(key = lambda i : i[0])

        for interval in intervals:
            start = interval[0]
            
            if start >= prev_end:
                prev_end = interval[1]
            else:
                overlaps += 1
                prev_end = min(prev_end, interval[1])

        return overlaps

