class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)-1
        n=0
        while m>=0 and n<=len(matrix[0])-1:
            if matrix[m][n]==target:
                return True
            elif matrix[m][n]>target:
                m=m-1
            elif matrix[m][n]<target:
                n=n+1
        return False