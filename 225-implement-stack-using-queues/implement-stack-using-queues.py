from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue1=deque()
        self.queue2=deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        q=self.queue1.popleft()
        self.queue1,self.queue2=self.queue2,self.queue1    
        return q    
    def top(self):
        """
        :rtype: int
        """
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        p=self.queue1[0]
        self.queue1.popleft()
        self.queue2.append(p)
        self.queue1,self.queue2=self.queue2,self.queue1
        return p
    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()