class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = list(bin(n)[2:])

        for i in range(len(binary)):
            if binary[i] == '0':
                binary[i] = '1'
        
        return int("".join(binary), 2)
        