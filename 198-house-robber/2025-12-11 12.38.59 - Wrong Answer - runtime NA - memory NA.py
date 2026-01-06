class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        do_not_rob = set()
        nums = [(-nums[i], i) for i in range(len(nums))]
        heapq.heapify(nums)

        amount = 0
        while nums:
            n, i = heapq.heappop(nums)
            if i in do_not_rob:
                continue
            amount += (-n)
            do_not_rob.add(i + 1)
            do_not_rob.add(i - 1)

        return amount

        