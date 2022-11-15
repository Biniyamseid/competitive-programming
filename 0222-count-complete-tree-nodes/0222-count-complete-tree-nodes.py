# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return 0
        def dfs(node):
            nonlocal count
            if not node:
                return 
            count +=1
            dfs(node.right)
            dfs(node.left)
            #count +=1
        dfs(root)
        return count
    
            