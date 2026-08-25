# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(current_node):
            if current_node is not None:
                current_node.left, current_node.right = current_node.right, current_node.left
                traverse(current_node.left)
                traverse(current_node.right)
        traverse(root)
        
        return root
        