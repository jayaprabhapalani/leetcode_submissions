# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and not head.next:
            return None
        #1. find the cycle first
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next

            if s==f:
                break
        else:
            return None # if no cycle return none
        #then if there is an cycle then find the cycle start position by moving the slow ptr to head and moving the s and f ptr one step at a time until they match
        s=head
        while s!=f:
            s=s.next
            f=f.next
        return s
       



        