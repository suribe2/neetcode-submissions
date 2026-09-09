"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        myHash = {}
        curr = head
        
        #get value into hash
        while curr:
            copy = Node(curr.val)
            myHash[curr] = copy
            curr = curr.next
        
        curr = head #reset curr back to head

        #loop through linked list again to ge .next and .random
        while curr:
            copy = myHash[curr]
            copy.next = myHash[curr.next] if curr.next else None
            copy.random = myHash[curr.random] if curr.random else None
            curr = curr.next
        

        if head is None:
            return None
        else:
            return myHash[head]
            
