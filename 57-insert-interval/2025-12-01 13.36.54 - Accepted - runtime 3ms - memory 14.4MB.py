class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)

        return self.merge(intervals)

    def merge(self, intervals):
        intervals.sort(key = lambda i : i[0])

        result = [intervals[0]]
        i = 1

        while i < len(intervals):
            current_pair = intervals[i]
            prev_pair = result[-1]

            if prev_pair[1] >= current_pair[0]:
                # merge
                result.pop()
                result.append([prev_pair[0], max(current_pair[1], prev_pair[1])])
            else:
                result.append(current_pair)

            i += 1

        return result

