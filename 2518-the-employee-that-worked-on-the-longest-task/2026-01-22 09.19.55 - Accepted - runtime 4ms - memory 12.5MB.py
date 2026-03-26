class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        start_time = 0
        max_work_time = (None, None) # (work_time, id)

        for id, leave_time in logs:
            work_time = leave_time - start_time
            if work_time == max_work_time[0]:
                max_work_time = (work_time, min(id, max_work_time[1]))
            else:
                max_work_time = max(max_work_time, (work_time, id))
            start_time = leave_time

        return max_work_time[1]
