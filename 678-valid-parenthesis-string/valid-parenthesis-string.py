class Solution(object):
    def checkValidString(self, s):
        left_min = 0 # Minimum possible open '('
        left_max = 0 # Maximum possible open '('
        
        for char in s:
            if char == "(":
                left_min += 1
                left_max += 1
            elif char == ")":
                left_min -= 1
                left_max -= 1
            else: # char == "*"
                left_min -= 1 # '*' acts as a right parenthesis ')'
                left_max += 1 # '*' acts as a left parenthesis '('
            
            # If the maximum possible open parentheses is negative, we have too many ')'
            if left_max < 0:
                return False
            
            # The minimum possible open parentheses cannot be negative.
            # If it drops below 0, it means a '*' we tried to use as a ')' 
            # should just be treated as an empty string instead.
            if left_min < 0:
                left_min = 0
                
        # The string is valid if we can perfectly match all parentheses, 
        # meaning the minimum open count drops to exactly 0.
        return left_min == 0 