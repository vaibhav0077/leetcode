# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        cycleFound = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                cycleFound = True
                fast = head
                break
        else: return None 
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow
        