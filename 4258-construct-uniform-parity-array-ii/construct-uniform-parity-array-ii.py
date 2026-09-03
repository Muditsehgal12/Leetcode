class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        m=float('inf')
        c1=0
        c2=0
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                c1+=1
            else:
                c2+=1
                m=min(m,nums1[i])
        if c1==len(nums1) or c2==len(nums1):
            return True  
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                if nums1[i]<m:
                    return False
        return True          