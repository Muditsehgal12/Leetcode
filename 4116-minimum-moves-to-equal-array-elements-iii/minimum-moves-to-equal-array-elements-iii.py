class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        a=max(nums)
        for i in nums:
            s+=a-i
        return s