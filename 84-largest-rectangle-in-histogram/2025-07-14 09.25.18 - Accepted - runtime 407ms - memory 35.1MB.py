class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        pse = {} 
        nse = {} 
    
        # compute PSE
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
    
        # compute NSE
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                prev_idx = stack.pop()
                nse[prev_idx] = i
            stack.append(i)

        # for values without a NSE, we assume the bar can stretch till the end of the list
        while stack:
            nse[stack.pop()] = n
    
        # compute max area
        max_area = 0
        for i in range(n):
            height = heights[i]
            width = nse[i] - pse[i] - 1
            area = height * width
            max_area = max(max_area, area)
    
        return max_area
        