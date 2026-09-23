class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total=sum(nums)
        target=total-x
        maxi=-1
        l=0
        curr=0
        if target==0:
            return len(nums)
        if target<0:
            return -1
        for r in range(len(nums)):
            curr+=nums[r]
            
            while curr>target:
                curr-=nums[l]
                l+=1
            if curr==target:
                maxi=max(maxi,r-l+1)
        if maxi==-1:
            return -1
        else:
            return len(nums)-maxi