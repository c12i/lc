class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        products, sums = getSumAndProduct(n)

        return n % (products + sums) == 0


def getSumAndProduct(n):
   products = 1
   sums = 0
   
   while n > 0:
       value = n % 10
       products *= value
       sums += value
       
       n = n // 10

   return products, sums
