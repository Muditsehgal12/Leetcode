class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length.
        if (m + n - 1) % 2 != 0:
            return False
        
        # Must start with an open bracket and end with a closed bracket.
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        memo = set()
        
        def dfs(r, c, balance):
            # If there are more closing brackets than opening ones at any point
            if balance < 0:
                return False
            
            # Pruning: The required closing brackets exceed the remaining steps
            if balance > (m - 1 - r) + (n - 1 - c):
                return False
                
            state = (r, c, balance)
            if state in memo:
                return False
                
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Move Down
            if r + 1 < m:
                next_bal = balance + (1 if grid[r + 1][c] == '(' else -1)
                if dfs(r + 1, c, next_bal):
                    return True
                    
            # Move Right
            if c + 1 < n:
                next_bal = balance + (1 if grid[r][c + 1] == '(' else -1)
                if dfs(r, c + 1, next_bal):
                    return True
            
            # Cache the failing state
            memo.add(state)
            return False
            
        return dfs(0, 0, 1)