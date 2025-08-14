class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        left = 0
        seen = defaultdict(int)
        max_num = float('-inf')
        ans = (0, 0)

        for right, n in enumerate(num):
            seen[n] += 1

            if right - left + 1 == 3:
                if len(seen) == 1:
                    candidate = next(iter(seen)) * seen[n]
                    if int(candidate) > max_num:
                        max_num = int(candidate)
                        ans = (left, right + 1)
                    
                if num[left] in seen:
                    seen[num[left]] -= 1
                    if seen[num[left]] == 0:
                        del seen[num[left]]
                left += 1

        l, r = ans
        return num[l:r]
