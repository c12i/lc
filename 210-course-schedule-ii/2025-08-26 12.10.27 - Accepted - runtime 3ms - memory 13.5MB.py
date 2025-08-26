class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjList = defaultdict(list)
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            inDegree[a] += 1
            adjList[b].append(a)

        stack = []

        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                stack.append(i)

        result = []

        while stack:
            curr = stack.pop()
            result.append(curr)

            adjacent = adjList[curr]
            for i in range(len(adjacent)):
                nxt = adjacent[i]
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    stack.append(nxt)

        return result if len(result) == numCourses else []