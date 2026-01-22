class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)
        
        # build list of all gaps (including 0 gaps)
        gaps = []
        
        # gap before first meeting
        gaps.append(max(0, startTime[0]))
        
        # gaps between meetings
        for i in range(n - 1):
            gap = startTime[i + 1] - endTime[i]
            gaps.append(gap)
        
        # gap after last meeting
        gaps.append(max(0, eventTime - endTime[n - 1]))
        
        # # edge case: if we need to consider more gaps than available
        # if k + 1 >= len(gaps):
        #     return sum(gaps)
        
        # use sliding window to find max sum of (k+1) consecutive gaps
        window_size = k + 1
        
        # initialize first window
        current_sum = sum(gaps[:window_size])
        max_result = current_sum
        
        # slide the window
        for i in range(window_size, len(gaps)):
            current_sum = current_sum - gaps[i - window_size] + gaps[i]
            max_result = max(max_result, current_sum)
        
        return max_result