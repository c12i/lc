class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        outdegree = [0] * n
        reverse_graph = [[] for _ in range(n)]

        for node in range(n):
            outdegree[node] = len(graph[node])
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)

        stack = [n for n in range(n) if outdegree[n] == 0]
        safe = []

        while stack:
            node = stack.pop()
            safe.append(node)

            for neighbor in reverse_graph[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    stack.append(neighbor)

        return sorted(safe)

        