class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr,l=head,0
        while curr!=None:
            l+=1
            curr=curr.next
        curr1,i=head,0
        while i < k-1:
            curr1=curr1.next
            i+=1
        curr2,j=head,0
        while j < l-k:
            curr2=curr2.next
            j+=1
        curr1.val,curr2.val=curr2.val,curr1.val
        return head       