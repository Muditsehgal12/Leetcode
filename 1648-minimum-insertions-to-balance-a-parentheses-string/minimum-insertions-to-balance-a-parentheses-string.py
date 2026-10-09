class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertions = 0
        right_needed = 0
        
        for char in s:
            if char == '(':
                # If we need an odd number of right parentheses, it means we have a 
                # single ')' that isn't paired up yet. We must balance it by inserting
                # one ')' right now before processing this new '('.
                if right_needed % 2 != 0:
                    insertions += 1
                    right_needed -= 1
                
                # A new '(' requires two '))'
                right_needed += 2
            else: # char == ')'
                right_needed -= 1
                
                # If right_needed drops below 0, it means we have a ')' without a preceding '('.
                # We must insert a '(' to balance it (1 insertion). That inserted '(' will 
                # also require one more ')' to complete the pair, so right_needed becomes 1.
                if right_needed < 0:
                    insertions += 1
                    right_needed += 2
                    
        # Add any remaining required right parentheses to the total insertions
        return insertions + right_needed