class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        hm = {}

        for i in range(len(arr1)):
            if hm.get(arr1[i]):
                hm[arr1[i]] += 1
            else:
                hm[arr1[i]] = 1
                 
                    
        for i in range(len(arr2)):
            if hm.get(arr2[i]):
                result.extend([arr2[i]] * hm[arr2[i]])
                del hm[arr2[i]]

        distinct = []

        for key in hm.keys():
            res = [key] * hm[key]
            distinct.extend(res)
        
        result.extend(self.countSort(distinct))

        return result


    def countSort(self, arr):
        max_val = -1

        for n in arr:
            max_val = max(max_val, n)

        count = [0] * (max_val + 1)

        for n in arr:
            count[n] += 1

        sorted_arr = []

        for num, freq in enumerate(count):
            sorted_arr.extend([num] * freq)

        return sorted_arr
