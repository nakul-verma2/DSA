class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Temporarily store the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev one step forward
            curr = next_node       # Move curr one step forward
            
        return prev