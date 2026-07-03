class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def revll(curr):
            prev=None
            while curr!=None:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        p2=revll(slow)
        p1=head
        max_sum=0
        while p1!=None and p2!=None:
            new=p1.val+p2.val
            max_sum=max(max_sum,new)
            p1=p1.next
            p2=p2.next
        return max_sum  