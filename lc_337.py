# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.recurse(root)
        return result[0] if result[0] > result[1] else result[1]
        
        
    def recurse(self, parent: TreeNode) -> (int, int):
        if not parent:
            return 0, 0
        
        if not (parent.left or parent.right):
            return 0, parent.val
        
        left = self.recurse(parent.left)
        right = self.recurse(parent.right)
                
        grandchildren_sum = max(left[0], left[1]) + max(right[0], right[1])
        children_sum = parent.val + left[0] + right[0]
    
        return (grandchildren_sum, children_sum)
        
