# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        p2=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                p1=fast
                if p1 == p2:
                    return p1
                while p1!=p2:
                    p1=p1.next
                    p2=p2.next
                    if p1==p2:
                        return p1   
                return None    
            