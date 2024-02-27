# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack != []:
            i = stack.pop()
            if isinstance(i, int):
                result.append(i)
            elif isinstance(i, TreeNode):
                result.extend([i, i.left, i.right])
        return result