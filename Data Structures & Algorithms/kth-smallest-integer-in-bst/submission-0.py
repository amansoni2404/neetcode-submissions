# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def traverse(current_node, result):
            if current_node.left is not None:
                traverse(current_node.left, result)
            result.append(current_node.val)
            if current_node.right is not None:
                traverse(current_node.right, result)

            return result
            
        result = traverse(root, result)
        print(result)
        return result[k-1]
        

        