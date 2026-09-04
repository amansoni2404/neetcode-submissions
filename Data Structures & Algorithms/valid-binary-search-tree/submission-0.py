# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        def traverse(current_node, result):
            if current_node.left is not None:
                traverse(current_node.left, result)
            result.append(current_node.val)
            if current_node.right is not None:
                traverse(current_node.right, result)
            return result
        in_order_traversal_array = traverse(root, result)
        for i in range(len(result)-1):
            if result[i] < result[i+1]:
                continue
            else:
                return False
        return True


        