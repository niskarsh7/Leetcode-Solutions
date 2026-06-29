class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        count=0
        while curr!=None :
            count+=1
            curr=curr.next
        curr2=head
        prev=dummy
        d=count-n+1
        #0 1 2 3 4 5
        #      p c 
        #d=4
        i=0
        while i < d-1 :
            curr2=curr2.next
            prev=prev.next
            i+=1
        prev.next=curr2.next
        return dummy.next