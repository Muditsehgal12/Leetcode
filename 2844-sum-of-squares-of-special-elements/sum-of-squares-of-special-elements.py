class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0
        
        # enumerate(nums, 1) starts the index 'i' at 1
        for i, num in enumerate(nums, 1):
            if n % i == 0:
                total_sum += num * num
                
        return total_sum