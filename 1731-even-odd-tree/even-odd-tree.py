# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        prev = -inf
        level = 0
        while queue:
            if level%2!=0:
                prev = float(inf)
            else:
                prev = -float(inf)
            for _ in range(len(queue)):
                curr = queue.popleft()
                c = curr.val
                if level%2==1:
                    if c%2 or c >=prev:
                        return False
                if level%2==0:
                    if c%2==0 or c<=prev:
                        return False
                prev = c
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
 
                
                print(curr.val)
            level+=1
        return True
