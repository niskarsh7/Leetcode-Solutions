class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def revll(curr):
            prev=None
            while curr!=None:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        p2=revll(slow)
        p1=head
        while p2!=None and p1!=None:
            if p2.val!=p1.val:
                return False
            p2=p2.next
            p1=p1.next 
        return True   