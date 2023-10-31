class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None 
        self.right = None 


class Tree:
    def __init__(self, val) -> None:
        self.root = TreeNode(val)


class Solution:
    def invertTree(self, root) -> None:
        if not root:
            return None

        self.left, self.right = self.invertTree(self.right), self.invertTree(self.left)

        return root
        

