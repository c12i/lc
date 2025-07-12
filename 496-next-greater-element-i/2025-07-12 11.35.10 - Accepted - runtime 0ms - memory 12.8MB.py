class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hm = {}

        for n in nums2:
            while stack:
                top = stack[-1]
                if n <= top:
                    break
                else:
                    t = stack.pop()
                    hm[t] = n
            
            # only pop in while loop, append afterwards after checks and pops are complete

            stack.append(n)

        result = []

        for n in nums1:
            if hm.get(n) is not None:
                result.append(hm[n])
            else:
                result.append(-1)

        return result
