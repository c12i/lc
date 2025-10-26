class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []

        def permutate(idx, curr = ""):
            if idx == len(s):
                ans.append(curr)
                return

            ch = s[idx]

            if ch.isdigit():
                permutate(idx + 1, curr + ch)
            else:
                permutate(idx + 1, curr + ch.lower())
                permutate(idx + 1, curr + ch.upper())

            idx -= 1

        permutate(0, "")

        return ans
