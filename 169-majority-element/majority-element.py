class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f={}
        for i in range(len(nums)):
            f[nums[i]]=f.get(nums[i],0)+1
        for i in f:
            if f[i]>len(nums)/2:
                return i
    
        