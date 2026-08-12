class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=0
        ans=0
        s={}
        while j<len(nums):
            s[nums[j]]=s.get(nums[j],0)+1
            while s[nums[j]]>k:
                maxi=j-i
                ans=max(maxi,ans)
                
                s[nums[i]]=s.get(nums[i])-1
                i+=1
            maxi=j-i+1
            j+=1
            
            ans=max(maxi,ans)
        return ans