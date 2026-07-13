# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #1. Size distribution
        #2. linked list distribution
        # dummmy noded not needed 
        length=0
        curr=head
        while curr!=None:
            length+=1
            curr=curr.next
        uniformNumber= length//k
        remainingNumber=length%k
        res = [None]*k
        curr=head
        for i in range(k):
            count=uniformNumber
            if remainingNumber>0:
                count+=1
                remainingNumber-=1
            if count==0:
                res[i]=None
                continue
            temp1=curr
            counter=0
            prev=None
            while counter < count:
                prev=curr
                curr=curr.next
                counter+=1
            prev.next=None
            res[i]=temp1
        return res