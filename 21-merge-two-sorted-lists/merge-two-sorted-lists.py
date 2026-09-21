class Solution:
    def mergehelper(self,list1,list2,curr):
        if (list1==None):
            curr.next=list2
            return
        if (list2==None):
            curr.next=list1
            return
        if (list1.val<=list2.val):
            curr.next=list1
            self.mergehelper(list1.next,list2,curr.next)
        else:
            curr.next=list2
            self.mergehelper(list2.next,list1,curr.next)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        self.mergehelper(list1,list2,curr)

        return dummy.next