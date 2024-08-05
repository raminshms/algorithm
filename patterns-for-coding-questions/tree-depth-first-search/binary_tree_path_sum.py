class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int):
    if not root:
        return False
    
    if root.val == targetSum and not root.left and not root.right:
        return True
    

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)



def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    # root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(hasPathSum(root, 23))
    print(hasPathSum(root, 16))


test()
