class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If 'opened' is greater than 0, it's not the outermost '('
                if opened > 0:
                    res.append(char)
                opened += 1
            elif char == ')':
                opened -= 1
                # If 'opened' is greater than 0 after decrementing, it's not the outermost ')'
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)