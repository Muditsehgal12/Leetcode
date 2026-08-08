class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in num:

            while k>0 and stack and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        while k > 0:
            stack.pop()
            k -= 1
        ans = ''.join(stack).lstrip('0')

        return ans if ans else "0"