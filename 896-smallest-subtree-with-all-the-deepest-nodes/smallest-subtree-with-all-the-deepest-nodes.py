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
        parent = {root.val:-1}
        indepth = []
        def par(Node):
            nonlocal parent
            if not Node:
                return 
            if Node.left:
                parent[Node.left.val] = Node.val
            if Node.right:
                parent[Node.right.val] = Node.val
            par(Node.left)
            par(Node.right)
        par(root)
        print(parent)
        
            
       
        single = []
        ans = []
        deepest = get_depth(root)
        def dfs(Node,tar):
            if not Node:
                return 0
            if Node.val ==tar:
                print("heloo")
                k = Node
                return K
                return [Node.val,Node.left.val,Node.right.val]
            left =  dfs(Node.left,tar)
            # if left:
            #     return left
            right =  dfs(Node.right,tar)
            # if right:
            #     return right
            # return 1 + max(dfs(Node.left),dfs(Node.right))
        def re(Node,target):
           
            if not Node:
                return 0
            print(Node.val,"Node.val",target)
            if Node.val == target:
                print("hello node.val==target")
                g = Node
                return g
            left = re(Node.left,target)
            if left:
                return left
            right = re(Node.right,target)
            if right:
                return right
        deepth_of_nodes = {}
        
        def sol(Node,depth):
            nonlocal ans
            nonlocal deepest
            if not Node:
                return depth
            deepth_of_nodes[Node.val]=depth
            if depth == deepest-1:
                indepth.append(Node.val)
            if depth == deepest-1 and (not Node.left and not Node.right):
                d = Node
                single.append(d)
            if depth == deepest-2 and (Node.left and Node.right):
                c = Node
                ans.append(c)
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
            print(self.answer)
            return self.answer
            return re(root,self.answer)

            # #find common ancestor of both
            # parenta = set()
            # parentb = set()
            # def traverse(val,p):
            #     if val==-1:
            #         return
            #     p.add(val)
            #     traverse(parent[val],p)
            # traverse(indepth[0],parenta)
            # traverse(indepth[1],parentb)
            # print(parenta,parentb)
            # answer = parenta.intersection(parentb)
            
            # answer = list(answer)
            # answer = sorted(answer,key  =lambda x: -deepth_of_nodes[x])
            # print("ans")
            # print(answer)
            # print(deepth_of_nodes)
            # return re(root,answer[0])

        print(indepth)
     
        if ans:
            return ans[0]
        if single:
            return single[0]
        else: 
            return root
       
        