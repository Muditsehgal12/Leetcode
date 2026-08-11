class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def ss(num):
            s=0
            a=0
            while num>0:
                a=num%10
                s=s+a*a
                num=num//10
            return s
        slow=ss(n)
        fast=ss(ss(n))
        while slow!=fast:
            slow=ss(slow)
            fast=ss(ss(fast))
        return slow==1
        