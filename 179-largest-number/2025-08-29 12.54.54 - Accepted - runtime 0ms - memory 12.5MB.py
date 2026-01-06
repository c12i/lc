class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_strings = [str(num) for num in nums]

        num_strings.sort(key=lambda a: a * 10, reverse=True)

        if num_strings[0] == "0":
            return "0"

        return "".join(num_strings)
        