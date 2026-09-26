class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        # Convert knowledge to a dictionary for O(1) lookups
        knowledge_dict = {k: v for k, v in knowledge}
        
        res = []
        cur_key = []
        in_bracket = False
        
        # Single O(N) pass through the string
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(cur_key)
                # Look up the key, default to "?" if not found
                res.append(knowledge_dict.get(key_str, "?"))
                # Reset current key
                cur_key = []
            elif in_bracket:
                cur_key.append(char)
            else:
                res.append(char)
                
        return "".join(res)