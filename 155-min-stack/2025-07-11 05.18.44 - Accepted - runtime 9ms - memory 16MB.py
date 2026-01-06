class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # push to stack
        # if current value <= minstack top value -> push to min stack
        self.stack.append(val)
        if not len(self.min_stack):
            self.min_stack.append(val)
        else:
            min_stack_top = self.min_stack[-1]
            if val <= min_stack_top:
                self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """

        # pop from stack
        # if stack_value == minstack top value -> pop from min stack
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]   
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()