class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        p = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                p[i][j] = matrix[n - 1 - j][i]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = p[i][j]