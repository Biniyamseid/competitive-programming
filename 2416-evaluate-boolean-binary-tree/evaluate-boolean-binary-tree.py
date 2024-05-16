# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # if not node.left and not node.right:
            #     return root.val !=0
            # evaluate_left_subtree = dfs(node.left)
            # evaluate_right_subtree = dfs(node.right)
            # if root.val ==2:
            #     evaluate_root = evaluate_left_subtree or evaluate_right_subtree
            # else:
            #     evaluate_root = evaluate_left_subtree and evaluate_right_subtree
            # return evaluate_root
            if not root.left and not root.right:
                # Handles the case for leaf nodes.
                return root.val != 0

            # Store the evaluations for the left subtree and right subtree.
            evaluate_left_subtree = dfs(root.left)
            evaluate_right_subtree = dfs(root.right)
            if root.val == 2:
                evaluate_root = evaluate_left_subtree or evaluate_right_subtree
            else:
                evaluate_root = evaluate_left_subtree and evaluate_right_subtree

            return evaluate_root
            
        return dfs(root)
       
        