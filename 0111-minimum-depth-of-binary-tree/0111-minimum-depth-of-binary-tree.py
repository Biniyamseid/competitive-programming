# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([(root,1)])
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node,cur_depth = queue.popleft()
                if not node.left and not node.right:
                    return cur_depth
                if node.left:
                    queue.append((node.left,cur_depth+1))
                if node.right:
                    queue.append((node.right,cur_depth+1))
        return cur_depth
        