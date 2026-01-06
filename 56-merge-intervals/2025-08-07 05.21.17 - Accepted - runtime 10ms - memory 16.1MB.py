class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        sorted_intervals = sorted(intervals, key = lambda i : i[0])

        result = [sorted_intervals[0]]
        i = 1

        while i < len(sorted_intervals):
            current_pair = sorted_intervals[i]
            prev_pair = result[-1]

            if prev_pair[1] >= current_pair[0]:
                # merge
                result.pop()
                result.append([prev_pair[0], max(current_pair[1], prev_pair[1])])
            else:
                result.append(current_pair)

            i += 1

        return result
