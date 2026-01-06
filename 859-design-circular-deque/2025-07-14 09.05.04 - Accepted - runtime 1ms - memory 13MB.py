class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.items = []
        self.max_size = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.items.insert(0, value)
        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.items.append(value)
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.items.pop(0)
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.items.pop()
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[0]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[len(self.items) - 1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.items) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.items) == self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()