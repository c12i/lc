class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = deque()
        temp = num

        while temp > 0:
            rem = temp % 10
            digits.appendleft(rem)
            temp = temp // 10

        l = len(digits)
        max_num = num

        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                max_num = max(max_num, self.digitsToNum(digits))
                digits[i] = 6

        return max_num
        

    def digitsToNum(self, digits):
        res = 0
        l = len(digits) - 1

        for d in digits:
            res += d * (10 ** l)
            l -= 1

        return res

