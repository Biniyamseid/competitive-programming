class Solution:
    def verticalTraversal(self, root):
        dic = defaultdict(list)
        self.min_l, self.max_l = float("inf"), -float("inf")
        def traverse(root, lvl_h, lvl_v):
            self.min_l = min(lvl_h, self.min_l)
            self.max_l = max(lvl_h, self.max_l)
            dic[lvl_h].append((lvl_v, root.val))
            if root.left:  traverse(root.left,  lvl_h-1, lvl_v+1)
            if root.right: traverse(root.right, lvl_h+1, lvl_v+1)
        
        traverse(root, 0, 0)
        out = []
        for i in range(self.min_l, self.max_l + 1):
            out += [[j for i,j in sorted(dic[i])]]
        return out