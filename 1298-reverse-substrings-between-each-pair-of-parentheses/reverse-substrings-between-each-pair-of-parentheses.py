class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        pair = {}
        
        # Step 1: Pair matching parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        i = 0
        direction = 1
        
        # Step 2: Traverse and "teleport" at brackets
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction
            
        return "".join(res)