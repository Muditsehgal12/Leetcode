class MyQueue(object):

    def __init__(self):
        
        self.stack1=[]
        self.stack2=[]
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack2:
            for i in range(len(self.stack1)-1,-1,-1):
                self.stack2.append(self.stack1[i])
            self.stack1=[]
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            for i in range(len(self.stack1)-1,-1,-1):
                self.stack2.append(self.stack1[i])
            self.stack1=[]
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()