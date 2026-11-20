# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = defaultdict(list)

        def traverse(root, level):
            if not root:
                return
            
            self.levels[level].append(root.val)

            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        
        traverse(root, 0)

        return [self.levels[level] for level in self.levels.keys()]
            

            
