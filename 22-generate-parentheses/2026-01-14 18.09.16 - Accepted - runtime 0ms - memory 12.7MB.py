class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(open_left = 0, close_left = 0, path = []):
            if open_left == n and close_left == n:
                result.append("".join(path))
            if open_left < n:
                path.append("(")
                backtrack(open_left + 1, close_left, path)
                path.pop()
            if close_left < open_left:
                path.append(")")
                backtrack(open_left, close_left + 1, path)
                path.pop()
        
        backtrack()
        return result
