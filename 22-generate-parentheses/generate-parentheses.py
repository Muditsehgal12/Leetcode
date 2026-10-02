class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(current_str, left_count, right_count):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            if left_count < n:
                backtrack(current_str + '(', left_count + 1, right_count)
            if right_count < left_count:
                backtrack(current_str + ')', left_count, right_count + 1)
                
        backtrack('', 0, 0)
        return res