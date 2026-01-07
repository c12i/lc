class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s

        # chars = s[1:][::-1]
        # curr_idx = 0

        # while chars[:curr_idx + 1] + s != (chars[:curr_idx + 1] + s)[::-1]:
        #     curr_idx += 1

        # return chars[:curr_idx + 1] + s

        reversed_s = s[::-1]
        combined = s + '#' + reversed_s

        # KMP prefix-function (LPS) over combined
        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length

        pal_prefix_len = lps[-1]
        # The part of s after the palindromic prefix must be mirrored in front
        to_prepend = reversed_s[:len(s) - pal_prefix_len]
        return to_prepend + s

    