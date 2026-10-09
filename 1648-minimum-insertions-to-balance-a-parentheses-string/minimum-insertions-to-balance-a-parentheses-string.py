class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertion=0
        need=0
        for i in s:
            if i=='(':
                if need%2!=0:
                    insertion+=1
                    need-=1
                need+=2
            else:
                need-=1
                if need<0:
                    insertion+=1
                    need+=2
        return need+insertion