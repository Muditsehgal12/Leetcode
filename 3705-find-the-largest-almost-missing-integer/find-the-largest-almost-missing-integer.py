class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        st=[]
        f={}
        for l in range(len(nums)-k+1):
                st=nums[l:l+k]
                for i in set(st):
                    f[i]=f.get(i,0)+1
                
        
        m=-1
        for i in f:
            if f[i]==1:
                m=max(m,i)
        return m


