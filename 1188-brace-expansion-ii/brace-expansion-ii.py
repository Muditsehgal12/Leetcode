class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = []
        res = []
        cur = []
        
        for c in expression:
            if c == '{':
                # Push current state to stack before entering a new brace group
                stack.append(res)
                stack.append(cur)
                res, cur = [], []
            elif c == '}':
                # Pop previous state and compute Cartesian product
                pre_cur = stack.pop()
                pre_res = stack.pop()
                
                # Combine everything inside the evaluated braces
                cur_set = set(res + cur)
                
                if not pre_cur:
                    cur = list(cur_set)
                else:
                    # Concatenate with the item(s) just before the '{'
                    new_cur = set()
                    for p in pre_cur:
                        for c_str in cur_set:
                            new_cur.add(p + c_str)
                    cur = list(new_cur)
                
                # Restore the previous 'res' list
                res = pre_res
            elif c == ',':
                # A comma means we take the union; push `cur` words to `res` 
                res.extend(cur)
                cur = []
            else:
                # Letters: Just concatenate to the current active sequence
                if not cur:
                    cur = [c]
                else:
                    cur = [s + c for s in cur]
                    
        # The answer must be a sorted list of unique words
        return sorted(list(set(res + cur)))