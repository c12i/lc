class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        best = float('-inf')
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0

        for right, x in enumerate(s):
            if x in vowels:
                vowel_count += 1 

            if right - left + 1 == k:
                y = s[left]
                if vowel_count > best:
                    best = vowel_count
                if y in vowels:
                    vowel_count -= 1
                left += 1
                
        return best
        