# Binary Tree Inorder Traversal
# And I will upload post and pre traversal as soon as possi
############################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack: 
            while root != None:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            res.append(root.val) 
            root = root.right 
        return res
