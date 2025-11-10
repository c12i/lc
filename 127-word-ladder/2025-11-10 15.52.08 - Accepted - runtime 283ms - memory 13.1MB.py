class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        seen = set([beginWord])
        
        while queue:
            word, dist = queue.popleft() 
            if word == endWord:
                return dist
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]

                    if next_word in word_set and next_word not in seen:
                        seen.add(next_word)
                        queue.append((next_word, dist + 1))

        return 0
