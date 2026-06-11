class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        counter = defaultdict(int)

        for days in responses:
            for r in set(days):
                counter[r] += 1
        
        max_freq = max(counter.values())
        ans = None

        for k in sorted(counter.keys(), reverse = True):
            if counter[k] == max_freq:
                ans = k
        
        return ans
