# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev_node = head
        if not prev_node or not prev_node.next or not prev_node.next.next:
            return [-1, -1]
            
        curr_node = head.next
        next_node = head.next.next
        
        first_critical = -1
        last_critical = -1
        min_distance = float('inf')
        
        index = 1
        while next_node is not None:
            # Check for local maxima or local minima
            if (curr_node.val > prev_node.val and curr_node.val > next_node.val) or \
               (curr_node.val < prev_node.val and curr_node.val < next_node.val):
                
                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(min_distance, index - last_critical)
                
                last_critical = index
                
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next
            index += 1
            
        if first_critical == -1 or first_critical == last_critical:
            return [-1, -1]
            
        max_distance = last_critical - first_critical
        return [min_distance, max_distance]