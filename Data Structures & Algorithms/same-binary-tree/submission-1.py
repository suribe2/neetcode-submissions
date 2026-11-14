# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p is None) and (q is None):
            return True

        if (p is None) != (q is None):
            return False

        if p.val != q.val:
            return False

        queue = deque([(p, q)])
        
        while queue:
            a, b = queue.popleft()
            if (a is None) != (b is None):
                return False
            if (a is None) and (b is None):
                continue
            elif a.val!= b.val:
                return False 
            queue.append((a.left, b.left))
            queue.append((a.right, b.right))
        return True

        