class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        for i in range(len(nums2)):
            nums1.append(nums2[i])
            nums1.sort()
        l=0
        r=len(nums1)-1
        if r%2==0:
            mid=(l+r)/2
            return nums1[mid]
        else:
            m1=(r+1)/2
            m2=(r-1)/2
            u=float(nums1[m1]+nums1[m2])/2
            return u