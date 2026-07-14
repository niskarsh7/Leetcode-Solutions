class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head.next
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next

            first.next=second.next
            second.next=first
            prev.next=second
            prev=first
        return dummy.next