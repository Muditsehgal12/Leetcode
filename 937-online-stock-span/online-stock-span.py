class StockSpanner(object):

    def __init__(self):
        
        self.stack=[]
        

    def next(self, price):
        c=1
        if self.stack==[]:
            self.stack.append((price,1))
            return 1
        while self.stack and self.stack[-1][0]<=price:
            c+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,c))

        return c    


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)