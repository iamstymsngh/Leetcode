from typing import  Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # All root to leaf paths
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        self.findPaths(root, paths, "")
        return paths

    def findPaths(self, root: Optional[TreeNode], paths: List[str], temp: str):
        if not root:
            return

        temp += str(root.val)
        temp += "->"
        if not root.left and not root.right:
            temp = temp[:-2]
            paths.append(temp)
            return

        self.findPaths(root.left, paths, temp[:])
        self.findPaths(root.right, paths, temp[:])
