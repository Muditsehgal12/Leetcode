# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        temp=slow.next
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        while prev:
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        return True