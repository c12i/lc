"""
n = 20
k = 5
counter = {
    'W': 6, 'Q': 3, 'E': 2, 'R': 1
}

ans = 5

W W E Q E R Q W Q W W R W W E R Q W E Q
                      L
                                      R
"""

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        counter = Counter(s)
        k = n // 4

        left = 0
        ans = float('inf')

        for right, ch in enumerate(s):
            counter[ch] -= 1

            while left < n and all(counter[ch] <= k for ch in counter):
                ans = min(ans, right - left + 1)
                counter[s[left]] += 1
                left += 1

        return ans
