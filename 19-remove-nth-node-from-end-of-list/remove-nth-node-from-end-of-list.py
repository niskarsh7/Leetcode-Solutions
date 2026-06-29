class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        jumps=0
        while jumps< n and curr!=None :
            jumps+=1
            curr=curr.next
        curr2=curr
        prev=dummy
        while curr2!=None :
            curr2=curr2.next
            prev=prev.next
        prev.next=prev.next.next
        return dummy.next