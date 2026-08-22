class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=0
        prod=1
        s=[]
        a=0
        p=n
        while n>0:
            a=n%10
            n=n//10
            s.append(a)
        for i in s:
            summ+=i
            prod*=i
        l=summ+prod
        return p%l==0