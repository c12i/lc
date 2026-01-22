class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        
        if len(s) > 12:
            return result
        
        def backtrack(idx=0, path=[]):
            if idx == len(s) and len(path) == 4:
                result.append(".".join(path))
                return
            if len(path) == 4:
                return
            
            for i in range(idx, len(s)):
                n = s[idx:i+1] 
                if (n.startswith('0') and len(n) > 1) or int(n) > 255:
                    continue
                path.append(n)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack()

        return result

