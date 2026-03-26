class ListNode(object):
    def __init__(self, value, nxt = None, prev = None):
        self.val = value
        self.next = nxt
        self.prev= prev


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.max_len = k
        self.len = 0
        self.head = None
        self.tail = None
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        new_node = ListNode(value)
        
        if self.isEmpty():
            self.tail = new_node
            self.head = new_node
        else:
            tail = self.tail
            new_node.next = tail
            tail.prev = new_node
            self.tail = new_node

        self.len += 1

        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.head or not self.tail:
            return False
        
        if self.len == 1:
            self.head = None
            self.tail = None
        else:
            head = self.head
            prev = self.head.prev
            prev.next = None
            self.head = prev

        self.len -= 1

        return True
        

    def Front(self):
        """
        :rtype: int
        """
        return self.head.val if self.head else -1
        

    def Rear(self):
        """
        :rtype: int
        """
        return self.tail.val if self.tail else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.max_len
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()