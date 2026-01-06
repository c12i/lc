class Solution(object):
    def canFinish(self, n, prerequisites):
        adjList = defaultdict(list)
        inDegree = [0] * n
        for a, b in prerequisites:
            adjList[b].append(a)
            inDegree[a] += 1

        if not 0 in inDegree:
            return False

        stack = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                stack.append(i)

        count = 0
        while stack:
            curr = stack.pop()
            count += 1

            adjacent = adjList[curr]

            for i in range(len(adjacent)):
                nxt = adjacent[i]
                inDegree[nxt] -= 1
                # if the inDegree value is now zero, push to stack
                if inDegree[nxt] == 0:
                    stack.append(nxt)

        # if no cycle, the count will be equal to n
        return count == n

    # def canFinish(self, n, prerequisites):
    #     adjList = defaultdict(list)
    #     for a, b in prerequisites:
    #         adjList[b].append(a)

    #     for v in range(n):
    #         queue = deque()
    #         seen = set()

    #         # add adjacent nodes for current vertex to queue
    #         adjacent = adjList[v]
    #         for i in range(len(adjacent)):
    #             queue.append(adjacent[i])
            
    #         while queue:
    #             curr = queue.popleft()
    #             seen.add(curr)

    #             if curr == v:
    #                 return False # cycle detected

    #             adjacent = adjList[curr]

    #             for i in range(len(adjacent)):
    #                 nxt = adjacent[i]
    #                 if nxt not in seen:
    #                     queue.append(nxt)

    #     return True
