class Solution:
    def score(self, cards: List[str], x: str) -> int:
        """
        :type cards: List[str]
        :type x: str
        :rtype: int
        """
        # {"a*": ["aa","ab","ac"], "*a": ["aa","ba"]}
        pat_map = {f"{x}*": [], f"*{x}": []}
        for s in cards:
            if s[0] == x:
                pat_map[f"{x}*"].append(s)
            if s[1] == x: 
                pat_map[f"*{x}"].append(s)

        points = 0
        for k in pat_map:
            l = len(pat_map[k])
            
            while l >= 2:
                l = l // 2
                points += 1

        return points