# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this is s and f ptr variable (maintain gap between ptrs)
        # just move the ptr one --f to n times
        #then move both , by the time the f ptr reaches the end , the slow's next ptr is at the node to be deleted
        #so just chnage the val then
        #deletion here- so hanlde this with dummy node
        dummy=ListNode(0)
        dummy.next=head

        s=dummy
        f=dummy

        for _ in range(n):
            f=f.next
        
        while f.next:
            s=s.next
            f=f.next
        s.next=s.next.next

        return dummy.next
    
        