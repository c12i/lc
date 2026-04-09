class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)

        max_heap = []
        for word, freq in counter.items():
            heapq.heappush(max_heap, (-freq, word))

        ans = [] 
        for i in range(k):
            _, word = heapq.heappop(max_heap)
            ans.append(word)

        return ans
