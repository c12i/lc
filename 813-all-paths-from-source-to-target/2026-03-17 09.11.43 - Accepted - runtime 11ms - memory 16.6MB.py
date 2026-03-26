class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = set()
        n = len(graph)
        res = []

        def dfs(node, path = []):
            path.append(node)
            if node ==  n - 1:
                res.append(path[:])
                return

            for ch in graph[node]:
                if ch not in visited:
                    visited.add(ch)
                    dfs(ch, path)
                    path.pop()
                    visited.remove(ch)

        dfs(0)

        return res
