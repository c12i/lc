class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.items = []
        self.max_size = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.items) < self.max_size:
            self.items.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop() if self.items else -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """

        if len(self.items) < k:
            for i in range(len(self.items)):
                self.items[i] += val
        else:        
            for i in range(k):
                self.items[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)