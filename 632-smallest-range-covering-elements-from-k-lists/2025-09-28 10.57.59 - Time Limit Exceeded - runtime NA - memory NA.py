"""
How much time have I spent, end-to-end?
Around 1 hour 30 minutes

What were the trickiest aspects? Where did you lose the most time?
- Terminating from the loop
- I was treating sorted lists as heaps

What are some lessons/insights I gained from this problem?
- sorted lists are not heaps

What would I do differently if I had extra time? What’s remaining to improve?
- Rethink solution and try make it more efficient.

What did I do well?
- I got the initial test cases passing, some TLE'd on submission

Did you use any hints, if yes, what? (please do not give up and look up the hints quickly. if you do need to look up the hints, only use the ones given on the problem page one by one, and DON'T look at youtube videos or full solutions, until you try really hard)
- I had a look at the discussion comments where a someone recommended heaps

How difficult was the problem (1 super trivial, 10 extremely difficult) (answer this question three times separately for a) implementing quickly b) finding the right approach c) overall)
a) 7 b) 9 c) 8

What's the time & space complexity?

Time: O(N log k) - Where N total number of elements in all lists, k number of lists
Space: O(N + k)
"""


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            heapq.heapify(nums[i])

        min_len = float('inf')
        ans = [0, 0]

        while True:
            lowest = (float('inf'), -1)
            highest = (float('-inf'), -1)

            for i in range(len(nums)):
                if not nums[i]: 
                    return ans
                lowest = min(lowest, (nums[i][0], i))
                highest = max(highest, (nums[i][0], i))

            diff = highest[0] - lowest[0]
            if diff < min_len:
                min_len = diff
                ans = [lowest[0], highest[0]]

            heapq.heappop(nums[lowest[1]])

        return ans