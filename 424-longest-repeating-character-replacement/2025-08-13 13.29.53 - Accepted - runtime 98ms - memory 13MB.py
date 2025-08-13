class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0

        seen = defaultdict(int)
        max_freq = float('-inf')
        max_len = float('-inf')

        for right, curr_char in enumerate(s):
            seen[curr_char] += 1
            max_freq = max(max_freq, seen[curr_char])
            curr_len = right - left + 1

            if curr_len - max_freq <= k:
                max_len = max(max_len, curr_len)
            else:
                seen[s[left]] -= 1
                left += 1

        return max_len
                