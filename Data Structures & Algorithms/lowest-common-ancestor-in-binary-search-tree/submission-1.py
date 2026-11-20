# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None
        def helper(root):
            if not root:
                return []
        
            left = helper(root.left)
            right = helper(root.right)

            com = left + right + [root.val]
            if p.val in com and q.val in com:
                if not self.ans:
                    self.ans = root
            return com
            
        helper(root)
        return self.ans
