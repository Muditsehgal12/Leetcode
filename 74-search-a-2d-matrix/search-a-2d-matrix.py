class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)//2
            a=mid//n
            b=mid%n
            if matrix[a][b]==target:
                return True
            elif matrix[a][b]>target:
                r=mid-1
            else:
                l=mid+1
        return False