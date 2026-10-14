class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        # If the required sum is greater than the maximum possible sum (all 9s)
        if sum > 9 * num:
            return ""
        
        res = []
        # Greedily take the maximum possible digit (up to 9 or the remaining sum)
        for _ in range(num):
            d = min(9, sum)
            res.append(str(d))
            sum -= d
            
        return "".join(res)