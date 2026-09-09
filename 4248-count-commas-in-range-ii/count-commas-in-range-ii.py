class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        ranges = [
            (1000, 999999, 1),
            (1000000, 999999999, 2),
            (1000000000, 999999999999, 3),
            (1000000000000, 999999999999999, 4),
            (1000000000000000, 10**15, 5)
        ]
        
        for start, end, commas in ranges:
            if n >= start:
                upper = min(n, end)
                total_commas += (upper - start + 1) * commas
                
        return total_commas