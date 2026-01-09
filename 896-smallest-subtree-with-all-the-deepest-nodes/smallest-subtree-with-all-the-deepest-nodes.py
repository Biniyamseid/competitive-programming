# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_depth(Node):
            if not Node:
                return 0
            return 1+ max(get_depth(Node.left),get_depth(Node.right))
        indepth = []
        single= []
        ans = []
        deepest = get_depth(root)
        deepth_of_nodes = {}
        
        def sol(Node,depth):
            nonlocal ans
            nonlocal deepest
            if not Node:
                return depth
            deepth_of_nodes[Node.val]=depth
            if depth == deepest-1:
                indepth.append(Node.val)
           
            sol(Node.left,depth+1)
            sol(Node.right,depth+1)
        sol(root,0)
        if len(indepth)==1:
            return TreeNode(indepth[0])
        else:
            k = len(indepth)
            self.answer = None
            def findanc(Node):
                if not Node:
                    return 0
                left =findanc(Node.left)
                right = findanc(Node.right)
                mid = 1 if Node.val in indepth else 0
                total = left + right + mid
                if total==k and self.answer == None:
                    self.answer = Node
                return total
            findanc(root)
            return self.answer

       
        