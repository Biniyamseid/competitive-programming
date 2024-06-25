# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []
        # start from right most and calculate the sum to the right and put it to current
        def dfs(node):
            if not node:
                return
            r=  dfs(node.left)
            nodes.append(node.val)
            l = dfs(node.right)
        dfs(root)
        nodes.reverse()
        def replace_values(node):
            if not node:
                return
            replace_values(node.left)
            replace_values(node.right)
            node_sum = 0
            for i in nodes:
                if i>node.val:
                    node_sum+=i
                else:
                    pass
            node.val+=node_sum
        replace_values(root)
        return root
            



        