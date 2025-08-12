class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == s:
            return t

        if not s or not t:
            return ""

        left = 0
        min_len = float('inf')
        ans = (0, 0)

        need = Counter(t)
        have = defaultdict(int)
        formed = 0
        required = len(need)

        for right, char in enumerate(s):
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = (left, right + 1)

                left_char = s[left]
                if left_char in need:
                    have[left_char] -= 1
                    if have[left_char] < need[left_char]:
                        formed -= 1

                left += 1

        l, r = ans

        return s[l:r] if min_len != float('inf') else ""

