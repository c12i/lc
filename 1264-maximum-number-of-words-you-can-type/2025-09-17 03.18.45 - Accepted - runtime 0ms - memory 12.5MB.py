class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split()
        broken = set(brokenLetters)

        count = 0

        for w in words:
            found = False
            for ch in w:
                if ch in broken:
                    found = True
                    break
                    
            if not found:
                count += 1

        return count
        