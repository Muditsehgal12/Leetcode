class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix=1
        c=-1
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                prefix*=nums[i]
            else:
                c=i
                count+=1
                continue
        ans = [0] * len(nums)
        if count>1:
            return ans
        elif count==1:
            for i in range(len(nums)):
                if i==c:
                    ans[i]=prefix
            return ans
        else:

            ans = [1] * len(nums)
            for i in range(len(nums)):
                ans[i]=prefix/nums[i]
            return ans