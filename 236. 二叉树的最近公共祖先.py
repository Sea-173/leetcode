# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.outside_result = []
        def findPath(root, target, path):
            print('root: ', root)
            if not root:
                return

            if root.val == target.val:
                print('path: ', path)
                path.append(root)
                self.outside_result = [z for z in path]
                print('self.outside_result: ', self.outside_result)
                return

            if root.left and self.outside_result == []:
                path.append(root)
                findPath(root.left, target, path)
                path.pop()

            if root.right and self.outside_result == []:
                path.append(root)
                findPath(root.right, target, path)
                path.pop()
        findPath(root, p, [])
        p_result = self.outside_result
        self.outside_result = []
        findPath(root, q, [])
        q_result = self.outside_result

        same_front = -1
        for i in range(min(len(p_result), len(q_result))):
            if p_result[i].val == q_result[i].val:
                same_front = p_result[i]
            else:
                break
        return same_front