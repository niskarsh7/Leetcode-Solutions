class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr!=None:
            l+=1
            curr=curr.next
        i=0
        curr1=head
        while i < k-1:
            curr1=curr1.next
            i+=1
        j=0
        curr2=head
        while j < l-k:
            curr2=curr2.next
            j+=1
        curr1.val,curr2.val=curr2.val,curr1.val
        return head       