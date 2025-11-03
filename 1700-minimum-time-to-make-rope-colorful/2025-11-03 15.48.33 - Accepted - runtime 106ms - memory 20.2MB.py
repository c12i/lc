class Solution(object):
    def minCost(self, colors, neededTime):
        n = len(colors)
        stack = []
        min_time = 0

        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            
            if colors[stack[-1]] == colors[i]:
                if neededTime[stack[-1]] < neededTime[i]:
                    min_time += neededTime[stack.pop()]
                    stack.append(i)
                else:
                    min_time += neededTime[i] 
            else:
                stack.append(i)

        return min_time