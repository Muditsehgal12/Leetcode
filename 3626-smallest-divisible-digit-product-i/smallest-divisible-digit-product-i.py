class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            a=str(n)
            l=[]
            ans=1
            for i in a:
                l.append(i)
                ans*=int(i)
            if ans%t==0:
                return n
                break
            n+=1
                