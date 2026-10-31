class Solution(object):

    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        next_cell = [[[None, None] for _ in xrange(n)] for _ in xrange(m)]

        
        for r in xrange(m - 1, -1, -1):
            for c in xrange(n - 1, -1, -1):
                if grid[r][c] == 0:
                    next_cell[r][c][0] = (r, c)
                    next_cell[r][c][1] = (r, c)
                else:
                    
                    if c + 1 < n:
                        next_cell[r][c][1] = next_cell[r][c + 1][0]
                    else:
                        next_cell[r][c][1] = None

                    
                    if r + 1 < m:
                        next_cell[r][c][0] = next_cell[r + 1][c][1]
                    else:
                        next_cell[r][c][0] = None

      
        dp = [[0] * n for _ in xrange(m)]
        dp[0][0] = 1

        for r in xrange(m):
            for c in xrange(n):
                if grid[r][c] == 0 and dp[r][c] > 0:
                    val = dp[r][c]

                    if c + 1 < n:
                        dest = next_cell[r][c + 1][0]
                        if dest is not None:
                            dr, dc = dest
                            dp[dr][dc] = (dp[dr][dc] + val) % MOD

                    if r + 1 < m:
                        dest = next_cell[r + 1][c][1]
                        if dest is not None:
                            dr, dc = dest
                            dp[dr][dc] = (dp[dr][dc] + val) % MOD

        return dp[m - 1][n - 1]