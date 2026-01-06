class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = Counter(nums)
        end = defaultdict(int)

        for n in nums:
            if not counter[n]: 
                continue
            counter[n] -= 1
            if end[n - 1]:
                end[n] += 1
                end[n - 1] -= 1
            elif counter[n + 1] and counter[n + 2]:
                counter[n + 1] -= 1
                counter[n + 2] -= 1
                end[n + 2] += 1
            else:
                return False

        return True