# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_nodes(node):
            if not node:
                return
            else:
                node.left, node.right = node.right, node.left
                swap_nodes(node.left)
                swap_nodes(node.right)
        
        nodes = root
        swap_nodes(nodes)
        return nodes