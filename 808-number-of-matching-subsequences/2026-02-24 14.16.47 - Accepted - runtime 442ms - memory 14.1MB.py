class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        buckets = defaultdict(list)
        
        for word in words:
            it = iter(word)
            buckets[next(it)].append(it)

        print(buckets)

        count = 0
        for ch in s:
            waiting = buckets[ch]
            buckets[ch] = []
            
            for it in waiting:
                nxt = next(it, None)
                if nxt is None:
                    count += 1
                else:
                    buckets[nxt].append(it)
        
        return count
