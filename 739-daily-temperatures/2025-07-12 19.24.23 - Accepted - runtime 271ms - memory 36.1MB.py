class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        hm = {} # map to keep track of the NGE idx at i
        
        for i in range(len(temperatures)):
            # if we are violating the decreasing monotonic stack rule
            while stack and temperatures[i] > temperatures[stack[-1]]:
                found = stack.pop()
                hm[found] = i

            stack.append(i)

        result = []

        for i in range(len(temperatures)):
            if hm.get(i) is not None:
                # compute diff between NGE idx and current idx
                result.append(hm[i] - i)                  
            else:
                result.append(0)

        return result