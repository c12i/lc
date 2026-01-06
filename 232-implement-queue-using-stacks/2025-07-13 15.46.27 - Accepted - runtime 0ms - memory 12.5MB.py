class MyQueue(object):

    def __init__(self):
        self.dequeue_stack = []
        self.enqueue_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.enqueue_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack.pop()
        elif len(self.enqueue_stack) > 0:
            self.__populate_dequeue_from_enqueue_stack()
            return self.dequeue_stack.pop()
        else:
            return None

        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack[-1]
        elif len(self.enqueue_stack) > 0:
            self.__populate_dequeue_from_enqueue_stack()
            return self.dequeue_stack[-1]
        else:
            return None
            

    def empty(self):
        """
        :rtype: bool
        """
        return (
            len(self.enqueue_stack) < 1 and 
            len(self.dequeue_stack) < 1
        )


    def __populate_dequeue_from_enqueue_stack(self):
        for i in range(len(self.enqueue_stack) - 1, -1, -1):
            self.dequeue_stack.append(self.enqueue_stack[i])
        self.enqueue_stack = []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()