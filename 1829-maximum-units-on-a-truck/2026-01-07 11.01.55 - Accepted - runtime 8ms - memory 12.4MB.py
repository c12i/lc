class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda item : item[1])

        loaded = 0

        while truckSize and boxTypes:
            num_boxes, num_units = boxTypes.pop()
            boxes_to_load = min(num_boxes, truckSize)
            loaded += (boxes_to_load * num_units)
            truckSize -= boxes_to_load

        return loaded