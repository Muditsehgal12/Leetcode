class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        level = {s}
        while True:
            # Check for valid strings in the current level
            valid_strings = filter(is_valid, level)
            
            # Since we remove one parenthesis at a time (BFS), the first level 
            # that contains valid strings has the minimum removals.
            if valid_strings:
                return valid_strings
            
            # If no valid strings, generate the next level by removing one parenthesis
            next_level = set()
            for string in level:
                for i in xrange(len(string)):
                    if string[i] in '()':
                        # Slice out the character at index i
                        next_level.add(string[:i] + string[i+1:])
            level = next_level