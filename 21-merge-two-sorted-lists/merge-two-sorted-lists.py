# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=list1
        head2=list2
        s=ListNode(0)
        temp=s

        while head1 and head2:
            if head1.val<head2.val:
                temp.next=head1
                temp=temp.next
                head1=head1.next
            else:
                temp.next=head2
                temp=temp.next
                head2=head2.next
        if not head1:
            temp.next=head2
        if not head2:
            temp.next=head1
        return s.next