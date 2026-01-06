class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        graph = defaultdict(list)

        for employee_id, manager_id in enumerate(manager):
            if manager_id != -1:
                graph[manager_id].append(employee_id)

        # bfs impl
        # queue = deque([(headId, 0)])
        # max_time = 0
        
        # while queue:
        #     emp_id, time = queue.popleft()
        #     max_time = max(max_time, time)

        #     for sub in graph[emp_id]:
        #         queue.append((sub, time + informTime[emp_id]))

        # return max_time

        for k in graph:
            subs = graph[k]
            graph[k] = (subs, informTime[k])

        return self.dfs(graph, headID)

    def dfs(self, graph, curr_id):
        if curr_id not in graph:
            return 0

        employees, informTime = graph[curr_id]
        max_time = 0

        for i in range(len(employees)):
            max_time = max(max_time, self.dfs(graph, employees[i]))

        return max_time + informTime
        
