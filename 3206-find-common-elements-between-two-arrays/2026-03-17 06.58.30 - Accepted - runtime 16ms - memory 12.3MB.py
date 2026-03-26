"""
answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
"""

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer1 = 0
        set2 = set(nums2)
        for n in nums1:
            if n in set2:
                answer1 += 1
        answer2 = 0
        set1 = set(nums1)
        for n in nums2:
            if n in set1:
                answer2 += 1
        return [answer1, answer2]