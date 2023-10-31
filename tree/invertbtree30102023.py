class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
def invertBinaryTree(rnode):
    if not rnode: 
        return None

    rnode.left, rnode.right = invertBinaryTree(rnode.right), invertBinaryTree(rnode.left)

    return rnode 
