# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        lst = []
        def dfs(root,cur):
            if not root:
                if cur:
                    lst.append(cur[::-1])
                return cur
            if root.left:
                dfs(root.left,cur+chr(ord("a")+int(root.left.val)))
            if root.right:
                dfs(root.right,cur+chr(ord("a")+int(root.right.val)))
            elif not root.right and not root.left:
                lst.append(cur[::-1])
                return cur
        dfs(root,chr(ord("a")+int(root.val)))
        return min(lst) if lst else ""

            
        