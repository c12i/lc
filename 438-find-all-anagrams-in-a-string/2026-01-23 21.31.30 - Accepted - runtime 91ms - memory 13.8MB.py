class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        counter = Counter(p)

        left = 0
        ans = []
        needed = len(counter)
        formed = 0

        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] == 0:
                    formed += 1

            while right - left + 1 > n:
                if s[left] in counter:
                    if counter[s[left]] == 0: 
                        formed -= 1
                    counter[s[left]] += 1
                left += 1
            
            if right - left + 1 == n and formed == needed:
                ans.append(left)
        
        return ans
