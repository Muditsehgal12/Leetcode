class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=nums[-1]-1
        b=nums[-2]-1
        return a*b
        