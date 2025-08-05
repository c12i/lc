class Solution(object):
    def groupAnagrams(self, strs):
        hm = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]
        return hm.values()
        