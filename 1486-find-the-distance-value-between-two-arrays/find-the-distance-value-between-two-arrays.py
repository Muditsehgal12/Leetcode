class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        i=0 
        c=0
        while i<len(arr1):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    break
            else:
                c+=1
            i+=1
        return c