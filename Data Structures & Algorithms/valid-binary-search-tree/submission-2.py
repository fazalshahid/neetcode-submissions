# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, lowerBound, higherBound):
            if not root:
                return True
            
            if root.val <= lowerBound or root.val >= higherBound:
                return False 

            return isValid(root.left, lowerBound, root.val) and isValid(root.right, root.val, higherBound)
        return isValid(root, -math.inf, math.inf)