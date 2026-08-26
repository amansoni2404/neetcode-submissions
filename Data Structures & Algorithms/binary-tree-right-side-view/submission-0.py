# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            qLen = len(queue)
            level = []
            for i in range(qLen):
                popped_element = queue.popleft()
                level.append(popped_element.val)
                if popped_element.left:
                    queue.append(popped_element.left)
                if popped_element.right:
                    queue.append(popped_element.right)
            if level:
                result.append(level[-1])
        return result
        