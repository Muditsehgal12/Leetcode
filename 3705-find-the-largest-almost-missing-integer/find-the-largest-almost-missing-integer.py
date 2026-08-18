class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        c=-1
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        if k==len(nums):
            return max(nums)
        elif k==1:
            for i in freq:
                if freq[i]==1:
                    c=max(c,i)
            return c
        else:
            
            candidates = []
            if freq[nums[0]] == 1:
                candidates.append(nums[0])
            if freq[nums[-1]] == 1:
                candidates.append(nums[-1])
            return max(candidates) if candidates else -1
