class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            p=0
            s=0
            a=nums[i]
            while a>0:
                p=a%10
                s+=p
                a=a//10
            if s==i:
                return i
        return -1