class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1,len(nums)+2):
            if k*i in nums:
                continue
            else:
                return k*i