"""
Time: O(N) where N is the number of chars in the string
Space: O(N)
"""
class Solution(object):
    def longestBeautifulSubstring(self, word):
        seen_chars = set()
        left = 0
        max_len = 0

        for right in range(len(word)):
            if right > 0 and word[right] < word[right - 1]:
                left = right
                seen_chars.clear()
                seen_chars.add(word[right])
            else:
                seen_chars.add(word[right])
            
            if len(seen_chars) == 5:
                max_len = max(max_len, right - left + 1)

        return max_len