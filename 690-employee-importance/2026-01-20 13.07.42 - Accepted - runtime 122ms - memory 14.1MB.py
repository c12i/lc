"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        adj_list = defaultdict(tuple)

        for employee in employees:
            adj_list[employee.id] = (employee.importance, employee.subordinates)

        queue = deque([id])
        total = 0

        while queue:
            emp_id = queue.popleft()
            importance, subordinates = adj_list[emp_id]
            total += importance

            for sub_id in subordinates:
                queue.append(sub_id)

        return total
