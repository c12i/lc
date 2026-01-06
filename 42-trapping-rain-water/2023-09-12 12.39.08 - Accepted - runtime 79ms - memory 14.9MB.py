class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_left = 0
        max_right = 0
        total = 0
        while i < j:
            if height[i] < height[j]:
                # act on left side
                if max_left < height[i]:
                    # update max_left
                    max_left = height[i]
                else:
                    # calculate water trapped
                    water = max_left - height[i]
                    # update total
                    total += water
                # increment height
                i += 1
            else:
                # act on right side
                if max_right < height[j]:
                    # update max_right
                    max_right = height[j]
                else:
                    # calculate water trapped
                    water = max_right - height[j]
                    # update total
                    total += water
                # decrement j
                j -= 1
        return total